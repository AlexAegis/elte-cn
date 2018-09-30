""" Network circuit simulator

uses cs1.json by default

Returns:
    void -- Network circuit simulation
"""

import json
import random
import colorsys
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation

# Build plot
FIG, AX = plt.subplots(figsize=(6, 4))
GRAPH = nx.Graph()


def iteration(i):
    """ an iteration of the simulation at the given position

    Arguments:
        i {int} -- current iteration
    """

    AX.clear()
    print "iteration: " + str(i + 1)

    # is there any new request?
    for demand in DATA["simulation"]["demands"]:
        if demand["start-time"] == i + 1:
            print "\tthere is a demand: " + str(demand)
            # is it a valid request?
            routes = possible_circuits(
                DATA["possible-circuits"], demand["end-points"][0], demand["end-points"][1])
            print "\tpossible routes for this demand: " + str(routes)

            if routes:

                found = False
                for route in routes:
                    if allocate_route(route, GRAPH.edges, demand, True) and not found:
                        allocate_route(route, GRAPH.edges, demand)
                        print "\t\troute allocated"
                        found = True
                    else:
                        print "\t\tcouldn't allocated route either because \
                                there is no bandwith or already found"

        # is there any requests to close?
        try_close_demand(demand, i)
    # this is for only drawing
    draw()


def try_close_demand(demand, i):
    """ Closes the demands that are no longer needed

    Arguments:
        demand {Demand} -- demand to check if its needed to be closed
        i {int} -- current iteration
    """

    if demand["end-time"] == i + 1:
        for edge in GRAPH.edges:
            if "demands" in GRAPH.edges[edge]:
                if demand in GRAPH.edges[edge]["demands"]:
                    GRAPH.edges[edge]["demands"].remove(demand)
                    if not GRAPH.edges[edge]["demands"]:
                        del GRAPH.edges[edge]["demands"]


def draw():
    """ Set the current state of the graph so when it gets drawn it will draw the updated values.
    """

    edge_has_demand = [(u, v)
                       for (u, v, d) in GRAPH.edges(data=True) if "demands" in d]
    edge_has_no_demand = [(u, v) for (u, v, d) in GRAPH.edges(
        data=True) if not "demands" in d]

    colors_has_demand = []
    widths_has_demand = []
    widths_has_no_demand = []

    for edge in edge_has_demand:
        rem = remaining_bandwith(GRAPH.edges[edge])
        random.seed(hash(str(GRAPH.edges[edge]["demands"])))
        color = colorsys.hsv_to_rgb(random.random(), 0.9, 0.9)
        hex_color = '#' + str(int(round(color[0] * 64))).zfill(2) + str(
            int(round(color[1] * 64))).zfill(2) + str(int(round(color[2] * 64))).zfill(2)
        colors_has_demand.append(hex_color)
        widths_has_demand.append(
            transform(GRAPH.edges[edge]["capacity"] - rem, 0, GRAPH.edges[edge]["capacity"], 8, 18))

    for edge in edge_has_no_demand:

        rem = remaining_bandwith(GRAPH.edges[edge])
        widths_has_no_demand.append(
            transform(rem, 0, GRAPH.edges[edge]["capacity"], 8, 18))

    # nodes
    nx.draw_networkx_nodes(GRAPH, POS, node_size=700)

    # edges
    nx.draw_networkx_edges(GRAPH, POS, edgelist=edge_has_demand,
                           width=widths_has_demand, edge_color=colors_has_demand)
    nx.draw_networkx_edges(GRAPH, POS, edgelist=edge_has_no_demand,
                           width=widths_has_no_demand, alpha=0.6)
    # labels
    nx.draw_networkx_labels(GRAPH, POS, font_size=20,
                            font_family='sans-serif', alpha=0.9)
    nx.draw_networkx_edge_labels(
        GRAPH, POS, font_size=8, font_family='sans-serif', alpha=0.7, bbox=dict(alpha=0.2))


def possible_circuits(circuits, point_a, point_b):
    """ takes a subset of the first argument's values whose values ends matches
    the values given in the first and the second argument

    Arguments:
        circuits {array<array<str>>} - - all the circuits
        point_a {str} - - requested starting point
        point_b {str} - - requested ending point

    Returns:
        array<array<str>> - - all the circuits what forms a route between this two points
    """

    result = []
    for circuit in circuits:
        if (circuit[0] == point_a and circuit[len(circuit) - 1] == point_b) \
                or (circuit[0] == point_b and circuit[len(circuit) - 1] == point_a):
            result.append(circuit)

    return result


def transform(old_val, old_min, old_max, new_min, new_max):
    """ transforms a value of a given range linearly into another range

    Arguments:
        old_val {int} -- original value
        old_min {int} -- original lower boundary
        old_max {int} -- original upper boundary
        new_min {int} -- new lower boundary
        new_max {int} -- new upper boundary

    Returns:
        int -- new value
    """
    return (((old_val - old_min) * (new_max - new_min)) / (old_max - old_min)) + new_min


def remaining_bandwith(edge):
    """ checks if an edge has enough bandwith or not

    Arguments:
        edge {map} -- an edge, containing information about the demands it already contains

    Returns:
        [int] -- the remaining bandwidth
    """
    available_bandwith = edge["capacity"]

    if "demands" in edge:
        for demand in edge["demands"]:
            available_bandwith = available_bandwith - demand["demand"]
    return available_bandwith


def allocate_route(route, edges, demand, test=False):
    """ Allocates a demand on a route onto a series of edges
    If its marked as test it wont perform the allocation just tests whether is possible or not

    Arguments:
        route {array<str>} -- array containing the start and end point
        edges {array<Edge>} -- the edges we want to perform our demand
        demand {Demand} -- the demand which contains the information about how much bandwith
                            it needs along the route

    Keyword Arguments:
        test {bool} -- is it just a test or not (default: {False})

    Returns:
        bool -- is it a valid allocation or not
    """

    valid = True
    for index, val in enumerate(route):
        if not index == 0:
            edge = edges[route[index - 1], val]
            # is there enough bandwith?
            available_bandwith = remaining_bandwith(edge)
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


with open(".\\lesson02\\cs1.json", "r") as _file:
    DATA = json.load(_file)

    for end_point in DATA["end-points"]:
        GRAPH.add_node(end_point, type="end-point")

    for switch in DATA["switches"]:
        GRAPH.add_node(switch, type="switch")

    for link in DATA["links"]:
        GRAPH.add_edge(link["points"][0], link["points"]
                       [1], capacity=link["capacity"])

    POS = nx.spring_layout(GRAPH)  # positions for all nodes
    # simulation
    # for i in range(data["simulation"]["duration"]):
    # iteration(i)

    ANIMATION = matplotlib.animation.FuncAnimation(
        FIG, iteration, frames=11, interval=500, repeat=True)
    plt.show()
