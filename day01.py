from itertools import *
from functools import *
from math import * 
import re
from collections import defaultdict 

from typing import *

data_file_name = "inputs/day1"
testing_file_name = data_file_name + "_test"

def part_1(filename):
    print(f"Part 1: {filename}")
    with open(filename) as file:
        ds = [int(line) for line in file]
        print(sum(b > a for a, b in zip(ds, ds[1:])))
        

def part_2(filename):
    print(f"Part 2: {filename}")
    with open(filename) as file:
        ds = [int(line) for line in file]
        triples = [sum(v) for v in zip(ds, ds[1:], ds[2:])]
        print(sum(b > a for a, b in zip(triples, triples[1:])))

if __name__ == "__main__":
    part_1(testing_file_name)
    part_1(data_file_name)
    part_2(testing_file_name)
    part_2(data_file_name)