from itertools import *
from functools import *
from math import * 
import re
from collections import defaultdict 

from typing import *


digit_re = re.compile(r"(\d+)")

data_file_name = "inputs/day11"
testing_file_name = data_file_name + "_test"

def adj(field, x, y):
    return ((x + xo, y + yo) for xo, yo in product([-1, 0, 1], [-1, 0, 1]) if x + xo >= 0 and x + xo < len(field[0]) and y + yo >= 0 and y + yo < len(field))

def part_1(filename):
    print(f"Part 1: {filename}")
    with open(filename) as file:
        field = [[int(v) for v in line.strip()] for line in file]
        #print(field)
        flashes = 0
        for step in range(100):
            #print(step)
            for row in field:
                for i in range(len(row)):
                    row[i] += 1
            
            flashed = set()
            while any(any(v > 9 and (x, y) not in flashed for x, v in enumerate(row)) for y, row in enumerate(field)):
                for y, row in enumerate(field):
                    for x, v in enumerate(row):
                        if v > 9 and (x, y) not in flashed:
                            flashed.add((x, y))
                            flashes += 1
                            for ax, ay in adj(field, x, y):
                                field[ay][ax] += 1
            for x, y in flashed:
                field[y][x] = 0
            print(flashes)

        print(flashes)


def part_2(filename):
    print(f"Part 2: {filename}")
    with open(filename) as file:        
        field = [[int(v) for v in line.strip()] for line in file]
        #print(field)
        flashes = 0
        step = 0
        while True:
            step += 1
            #print(step)
            for row in field:
                for i in range(len(row)):
                    row[i] += 1
            
            flashed = set()
            while any(any(v > 9 and (x, y) not in flashed for x, v in enumerate(row)) for y, row in enumerate(field)):
                for y, row in enumerate(field):
                    for x, v in enumerate(row):
                        if v > 9 and (x, y) not in flashed:
                            flashed.add((x, y))
                            flashes += 1
                            for ax, ay in adj(field, x, y):
                                field[ay][ax] += 1
            for x, y in flashed:
                field[y][x] = 0
            if len(flashed) == len(field) * len(field[0]):
                print(step)
                return


        pass

if __name__ == "__main__":
    part_1(testing_file_name)
    part_1(data_file_name)
    part_2(testing_file_name)
    part_2(data_file_name)