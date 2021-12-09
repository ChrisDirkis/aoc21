from itertools import *
from functools import *
from math import * 
import re
from collections import defaultdict 

from typing import *

data_file_name = "inputs/day9"
testing_file_name = data_file_name + "_test"

four_offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def four_neighbours(field, x, y):
    return [(nx + x, ny + y) for nx, ny in four_offsets if nx + x >= 0 and nx + x < len(field[0]) and ny + y >= 0 and ny + y < len(field)]


def part_1(filename):
    print(f"Part 1: {filename}")
    with open(filename) as file:
        field = [[int(v) for v in line.strip()] for line in file]
        s = 0
        for j in range(len(field)):
            for i in range(len(field[0])):
                if all(field[ny][nx] > field[j][i] for nx, ny in four_neighbours(field, i, j)):
                    s += field[j][i] + 1
        print(s)

def part_2(filename):
    print(f"Part 2: {filename}")
    with open(filename) as file:
        field = [[int(v) for v in line.strip()] for line in file]
        lows = []
        for j in range(len(field)):
            for i in range(len(field[0])):
                if all(field[ny][nx] > field[j][i] for nx, ny in four_neighbours(field, i, j)):
                    lows.append((i, j))
        
        basins = []
        for low in reversed(lows):

            s = 0
            frontier = [low]
            print(low)
            while frontier:
                x, y = frontier[0]
                frontier = frontier[1:]
                field[y][x] = -1
                s += 1
                #print(f"visiting {x} {y}")
                for nx, ny in four_neighbours(field, x, y):
                    if field[ny][nx] != -1 and field[ny][nx] != 9 and (nx, ny) not in frontier:
                        frontier.append((nx, ny))
            basins.append(s)
            #for line in field:
                #print(["_" if v == -1 else str(v) for v in line])
            #print(s)
        print(prod(sorted(basins)[-3:]))


if __name__ == "__main__":
    part_1(testing_file_name)
    part_1(data_file_name)
    part_2(testing_file_name)
    part_2(data_file_name)