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
        count = 0
        last = ds[0]
        for d in ds[1:]:
            if d > last:
                count += 1
            last = d
        print(count)
        

def part_2(filename):
    print(f"Part 2: {filename}")
    with open(filename) as file:
        ds = [int(line) for line in file]
        count = 0
        last = ds[0] + ds[1] + ds[2]
        for d1, d2, d3 in zip(ds[1:], ds[2:], ds[3:]):
            s = d1 + d2 + d3
            if s > last:
                count += 1
            last = s
        print(count)

if __name__ == "__main__":
    part_1(testing_file_name)
    part_1(data_file_name)
    part_2(testing_file_name)
    part_2(data_file_name)