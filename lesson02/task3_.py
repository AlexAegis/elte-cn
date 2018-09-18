import this
import json


class Simulation:
    endPoints = []
    demands = []
    duration = 0

    def __init__(self, duration):
        self.duration = duration

    def addDemand(self, demand):
        self.demands.append(demand)

    def run(self):
        for i in range(duration):
            print (i + 1)


class Demand:
    start = 0
    end = 0
    demand = 0


class Link:
    points = []  # 2 at most
    capacity = 0


def possibleCircuits(circuits, pointA, pointB):
    result = []
    for circuit in circuits:
        if (circuit[0] == pointA and circuit[len(circuits) - 1] == pointB) or (circuit[0] == pointB and circuit[len(circuits) - 1] == pointA):
            result.append(circuit)

    return result


with open(".\\lesson02\\cs1.json", "r") as file:
    data = json.load(file)

    # simulation
    simulation = data["simulation"]
    demands = simulation["demands"]
    duration = simulation["duration"]

    # sim = Simulation(duration)
    # sim.addDemand
    # sim.run()

    currentDemands = []
    for i in range(duration):
        print (i + 1)

        # is there any new request?
        for demand in demands:
            if demand["start-time"] == i + 1:
                # is it a valid request?
                currentDemands.append(demand)
                print demand

        # is there any requests to close?
        for demand in currentDemands:
            if demand["end-time"] == i + 1:
                currentDemands.remove(demand)
                print demand
