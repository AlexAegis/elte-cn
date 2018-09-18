import this
import json


class Simulation:
    endPoints = []


class Link:
    points = []  # 2 at most
    capacity = 0


with open(".\\lesson02\\cs1.json", "r") as file:
    data = json.load(file)

    # simulation
    simulation = data["simulation"]
    demands = simulation["demands"]
    duration = simulation["duration"]

    for i in range(duration):
        curr_demands = []
        demands = map(lambda d: 1, demands)
        print i
        print demands
