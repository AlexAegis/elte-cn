import this
import json
import networkx as nx
import matplotlib.pyplot as plt


def possibleCircuits(circuits, pointA, pointB):
    result = []
    for circuit in circuits:
        if (circuit[0] == pointA and circuit[len(circuit) - 1] == pointB) or (circuit[0] == pointB and circuit[len(circuit) - 1] == pointA):
            result.append(circuit)

    return result


def allocateRoute(route, edges, demand, test=False):
    valid = True
    for index, val in enumerate(route):
        if not index == 0:
            edge = edges[route[index - 1], val]

            # is there enough bandwith?
            available_bandwith = edge["capacity"]

            if "demand" in edge:
                available_bandwith = available_bandwith - \
                    edge["demand"]["demand"]

            if available_bandwith - demand["demand"] < 0:
                # invalid no bandwith left
                print "\tINVALID DEMAND, NO BANDWITH LEFT ON EDGE"
                valid = False
            else:
                if not test:
                    edge["demand"] = demand
                    print "\t\tedges along the route appended with the demand: from: " + \
                        str(route[index - 1]) + " to: " + \
                        str(val) + " edge: " + str(edge)
    return valid


g = nx.Graph()

with open(".\\lesson02\\cs1.json", "r") as file:
    data = json.load(file)

    for end_point in data["end-points"]:
        g.add_node(end_point, type="end-point")

    for switch in data["switches"]:
        g.add_node(switch, type="switch")

    for link in data["links"]:
        g.add_edge(link["points"][0], link["points"]
                   [1], capacity=link["capacity"])

    # simulation
    for i in range(data["simulation"]["duration"]):
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
                    gen = (route for route in routes if not found)
                    for route in gen:
                        if allocateRoute(route, g.edges, demand, True):
                            allocateRoute(route, g.edges, demand)
                            print "\t\troute allocated"
                            found = True
                        else:
                            print "\t\tcouldn't allocated route"

            # is there any requests to close?
            if demand["end-time"] == i + 1:
                for edge in g.edges:
                    if "demand" in g.edges[edge]:
                        if g.edges[edge]["demand"] == demand:
                            print "\tdelete demand between: " + str(edge) + " demand: " +\
                                str(g.edges[edge]["demand"])
                            del g.edges[edge]["demand"]

            # this is for only drawing
    pos = nx.spring_layout(g)  # positions for all nodes
    edges = [(u, v) for (u, v, d) in g.edges(data=True)]
    # nodes
    nx.draw_networkx_nodes(g, pos, node_size=700)

    # edges
    nx.draw_networkx_edges(g, pos, edgelist=edges,
                           width=6)
    # labels
    nx.draw_networkx_labels(g, pos, font_size=20, font_family='sans-serif')
    nx.draw_networkx_edge_labels(
        g, pos, font_size=12, font_family='sans-serif')

    plt.axis('off')
    plt.show()
