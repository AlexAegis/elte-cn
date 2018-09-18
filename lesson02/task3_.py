import this
import json
import networkx as nx
import matplotlib.pyplot as plt


class Simulation:
    endPoints = []
    demands = []
    duration = 0

    def __init__(self, duration):
        self.duration = duration

    def addDemand(self, demand):
        self.demands.append(demand)

    def run(self):
        for i in range(self.duration):
            print (i + 1)


def possibleCircuits(circuits, pointA, pointB):
    result = []
    for circuit in circuits:
        if (circuit[0] == pointA and circuit[len(circuits) - 1] == pointB) or (circuit[0] == pointB and circuit[len(circuits) - 1] == pointA):
            result.append(circuit)

    return result


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
    currentDemands = []
    for i in range(data["simulation"]["duration"]):
        print (i + 1)

        # is there any new request?
        for demand in data["simulation"]["demands"]:
            if demand["start-time"] == i + 1:
                # is it a valid request?
                currentDemands.append(demand)
                print demand

        # is there any requests to close?
        for demand in currentDemands:
            if demand["end-time"] == i + 1:
                currentDemands.remove(demand)
                print demand

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
