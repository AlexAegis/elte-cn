
import json
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation
import time
import colorsys
import random

# Build plot
fig, ax = plt.subplots(figsize=(6, 4))
g = nx.Graph()


def iteration(i):
    ax.clear()
    print "iteration: " + str(i + 1)

    # is there any new request?
    for demand in data["simulation"]["demands"]:
        if demand["start-time"] == i + 1:
            print "\tthere is a demand: " + str(demand)
            # is it a valid request?
            routes = possibleCircuits(
                data["possible-circuits"], demand["end-points"][0], demand["end-points"][1])
            print "\tpossible routes for this demand: " + str(routes)

            if len(routes) > 0:

                found = False
                for route in routes:
                    if allocateRoute(route, g.edges, demand, True) and not found:
                        allocateRoute(route, g.edges, demand)
                        print "\t\troute allocated"
                        found = True
                    else:
                        print "\t\tcouldn't allocated route either because there is no bandwith or already found"

        # is there any requests to close?
        if demand["end-time"] == i + 1:
            for edge in g.edges:
                if "demands" in g.edges[edge]:
                    if demand in g.edges[edge]["demands"]:
                        g.edges[edge]["demands"].remove(demand)
                        if len(g.edges[edge]["demands"]) == 0:
                            del g.edges[edge]["demands"]

    # this is for only drawing

    edges = [(u, v) for (u, v, d) in g.edges(data=True)]

    edge_has_demand = [(u, v)
                       for (u, v, d) in g.edges(data=True) if "demands" in d]
    edge_has_no_demand = [(u, v) for (u, v, d) in g.edges(
        data=True) if not "demands" in d]

    colors_has_demand = []
    widths_has_demand = []
    widths_has_no_demand = []

    for edge in edge_has_demand:
        rem = remainingBandwith(g.edges[edge])
        random.seed(hash(str(g.edges[edge]["demands"])))
        color = colorsys.hsv_to_rgb(random.random(), 0.9, 0.9)
        c = '#' + str(int(round(color[0] * 64))).zfill(2) + str(
            int(round(color[1] * 64))).zfill(2) + str(int(round(color[2] * 64))).zfill(2)
        print c
        colors_has_demand.append(c)
        widths_has_demand.append(
            transform(g.edges[edge]["capacity"] - rem, 0, g.edges[edge]["capacity"], 8, 18))

    for edge in edge_has_no_demand:

        rem = remainingBandwith(g.edges[edge])
        widths_has_no_demand.append(
            transform(rem, 0, g.edges[edge]["capacity"], 8, 18))

    # nodes
    nx.draw_networkx_nodes(g, pos, node_size=700)

    # edges
    nx.draw_networkx_edges(g, pos, edgelist=edge_has_demand,
                           width=widths_has_demand, edge_color=colors_has_demand)
    nx.draw_networkx_edges(g, pos, edgelist=edge_has_no_demand,
                           width=widths_has_no_demand, alpha=0.6)
    # labels
    nx.draw_networkx_labels(g, pos, font_size=20,
                            font_family='sans-serif', alpha=0.9)
    nx.draw_networkx_edge_labels(
        g, pos, font_size=8, font_family='sans-serif', alpha=0.7, bbox=dict(alpha=0.2))


def possibleCircuits(circuits, pointA, pointB):
    result = []
    for circuit in circuits:
        if (circuit[0] == pointA and circuit[len(circuit) - 1] == pointB) or (circuit[0] == pointB and circuit[len(circuit) - 1] == pointA):
            result.append(circuit)

    return result


def transform(OldValue, OldMin, OldMax, NewMin, NewMax):
    return (((OldValue - OldMin) * (NewMax - NewMin)) / (OldMax - OldMin)) + NewMin


def remainingBandwith(edge):
     # is there enough bandwith?
    available_bandwith = edge["capacity"]

    if "demands" in edge:
        #print "shit you not" + str(edge["demands"])
        for demand in edge["demands"]:
            #print "!!!! ITER DEMAND REM"
            available_bandwith = available_bandwith - \
                demand["demand"]
    return available_bandwith


def allocateRoute(route, edges, demand, test=False):
    valid = True
    for index, val in enumerate(route):
        if not index == 0:
            edge = edges[route[index - 1], val]
            # is there enough bandwith?
            available_bandwith = remainingBandwith(edge)
            if available_bandwith - demand["demand"] < 0:
                # invalid no bandwith left
                print "\tINVALID DEMAND, NO BANDWITH LEFT ON EDGE"
                valid = False
            else:
                if not test:
                    if not "demands" in edge:
                        edge["demands"] = []
                    edge["demands"].append(demand)
                    print "\t\tedges along the route appended with the demand: from: " + \
                        str(route[index - 1]) + " to: " + \
                        str(val) + " edge: " + str(edge)
    return valid


with open(".\\lesson02\\cs1.json", "r") as file:
    data = json.load(file)

    for end_point in data["end-points"]:
        g.add_node(end_point, type="end-point")

    for switch in data["switches"]:
        g.add_node(switch, type="switch")

    for link in data["links"]:
        g.add_edge(link["points"][0], link["points"]
                   [1], capacity=link["capacity"])

    pos = nx.spring_layout(g)  # positions for all nodes
    # simulation
    # for i in range(data["simulation"]["duration"]):
    # iteration(i)

    ani = matplotlib.animation.FuncAnimation(
        fig, iteration, frames=11, interval=500, repeat=True)
    plt.show()
