from itertools import *
from functools import *
from math import * 
import re
from collections import defaultdict 

from grid import *

digit_re = re.compile(r"(\d+)")

aod_day = str(int(__file__.split("/")[-1][3:5]))
data_file_name = "inputs/day" + aod_day
testing_file_name = data_file_name + "_test"

def part_1(filename):
    print(f"Part 1: {filename}")
    with open(filename) as file:
        edges = [line.strip().split("-") for line in file]
        graph = defaultdict(lambda: [])
        for edge in edges:
            gea = graph[edge[0]]
            gea.append(edge[1])
            
            geb = graph[edge[1]]
            geb.append(edge[0])

        caves = list(graph.keys())
        smalls = set(cave for cave in caves if cave.lower() == cave)

        ends = 0
        frontier = [["start"]]
        while frontier:
            path = frontier.pop()
            cave = path[-1]
            for jcave in graph[cave]:
                if jcave == "end":
                    ends += 1
                elif jcave in smalls:
                    if jcave not in path:
                        frontier.append(path + [jcave])
                else: 
                    frontier.append(path + [jcave])
        print(ends)
            
        pass

def part_2(filename):
    print(f"Part 2: {filename}")
    with open(filename) as file:
        edges = [line.strip().split("-") for line in file]
        graph = defaultdict(lambda: [])
        for edge in edges:
            gea = graph[edge[0]]
            gea.append(edge[1])
            
            geb = graph[edge[1]]
            geb.append(edge[0])
        
        caves = list(graph.keys())

        for cave in caves:
            if "start" in graph[cave]:
                graph[cave].remove("start") 

        smalls = set(cave for cave in caves if cave.lower() == cave )

        ends = 0
        frontier = [(["start"], None)]
        while frontier:
            path, dcave = frontier.pop()
            cave = path[-1]
            for jcave in graph[cave]:
                if jcave == "end":
                    ends += 1
                elif jcave in smalls:
                    if jcave not in path:
                        frontier.append((path + [jcave], dcave))
                    elif jcave in path and dcave == None:
                        frontier.append((path + [jcave], jcave))

                else: 
                    frontier.append((path + [jcave], dcave))
        print(ends)
        pass

if __name__ == "__main__":
    part_1(testing_file_name)
    part_1(data_file_name)
    part_2(testing_file_name)
    part_2(data_file_name)