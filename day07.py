from itertools import *
from functools import *
from math import * 
import re
from collections import defaultdict 

from typing import *

data_file_name = "inputs/day7"
testing_file_name = data_file_name + "_test"



def part_1(filename):
    print(f"Part 1: {filename}")
    with open(filename) as file:
        crabs = [int(v) for v in file.read().split(",")]
        minc = min(crabs)
        maxc = max(crabs)
        costs = [(sum(abs(crab - v) for crab in crabs), v) for v in range(minc, maxc + 1)]
        print(sorted(costs))

def part_2(filename):
    print(f"Part 2: {filename}")
    with open(filename) as file:
        crabs = [int(v) for v in file.read().split(",")]
        minc = min(crabs)
        maxc = max(crabs)
        costs = [(sum((abs(crab - v)**2 + abs(crab - v)) / 2 for crab in crabs), v) for v in range(minc, maxc + 1)]
        print(sorted(costs))

if __name__ == "__main__":
    part_1(testing_file_name)
    part_1(data_file_name)
    part_2(testing_file_name)
    part_2(data_file_name)