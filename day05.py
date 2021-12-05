from itertools import *
from functools import *
from math import * 
import re
from collections import defaultdict 

from typing import *

data_file_name = "inputs/day5"
testing_file_name = data_file_name + "_test"

# 0,9 -> 5,9

def get_line(line):
    [a, b] = line.split(" -> ")
    [x1, y1] = a.split(",")
    [x2, y2] = b.split(",")
    return ((int(x1), int(y1)), (int(x2), int(y2)))


def part_1(filename):
    print(f"Part 1: {filename}")
    with open(filename) as file:
        ls = [get_line(line) for line in file]
        max_x = max(max(l[1][0] for l in ls), max(l[0][0] for l in ls)) + 1
        max_y = max(max(l[1][1] for l in ls), max(l[0][1] for l in ls)) + 1
        field = [[0] * max_x for y in range(max_y)]
        for s, e in ls:
            if s[0] == e[0]:
                # vert
                sy = s[1]
                ey = e[1]
                if sy > ey:
                    ey, sy = sy, ey
                for y in range(sy, ey + 1):
                    field[s[0]][y] += 1
            if s[1] == e[1]:
                # horiz
                sx = s[0]
                ex = e[0]
                if sx > ex:
                    ex, sx = sx, ex
                for x in range(sx, ex + 1):
                    field[x][s[1]] += 1
        s = 0
        for x in range(max_x):
            for y in range(max_y):
                if field[x][y] > 1:
                    s += 1
        print(s)

def part_2(filename):
    print(f"Part 2: {filename}")
    with open(filename) as file:        
        ls = [get_line(line) for line in file]
        max_x = max(max(l[1][0] for l in ls), max(l[0][0] for l in ls)) + 1
        max_y = max(max(l[1][1] for l in ls), max(l[0][1] for l in ls)) + 1
        field = [[0] * max_x for y in range(max_y)]
        for s, e in ls:
            if s[0] == e[0]:
                # vert
                sy = s[1]
                ey = e[1]
                if sy > ey:
                    ey, sy = sy, ey
                for y in range(sy, ey + 1):
                    field[s[0]][y] += 1
            elif s[1] == e[1]:
                # horiz
                sx = s[0]
                ex = e[0]
                if sx > ex:
                    ex, sx = sx, ex
                for x in range(sx, ex + 1):
                    field[x][s[1]] += 1
            else:
                # diagonal
                if e[0] < s[0]:
                    s, e = e, s
                steps = e[0] - s[0] + 1
                direc = 1 if e[1] > s[1] else -1
                for i in range(steps):
                    x = s[0] + i
                    y = s[1] + i * direc
                    field[x][y] += 1
            
        s = 0
        for x in range(max_x):
            for y in range(max_y):
                if field[x][y] > 1:
                    s += 1
        print(s)

if __name__ == "__main__":
    part_1(testing_file_name)
    part_1(data_file_name)
    part_2(testing_file_name)
    part_2(data_file_name)