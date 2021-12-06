from itertools import *
from functools import *
from math import * 
import re
from collections import defaultdict 

from typing import *

data_file_name = "inputs/day6"
testing_file_name = data_file_name + "_test"

def part_1(filename, days):
    print(f"Part 1: {filename}")
    with open(filename) as file:
        fish = [int(v) for v in re.findall(r"(\d+)", file.readline())]
        for day in range(days):
            zeros = sum(f == 0 for f in fish)
            fish = [f - 1 if f > 0 else 6 for f in fish]
            for _ in range(zeros):
                fish.append(8)
        print(sum(True for f in fish))


def part_2(filename, days):
    print(f"Part 2: {filename}")
    with open(filename) as file:

        fish = [int(v) for v in re.findall(r"(\d+)", file.readline())]
        fd = dict()
        for age in range(9):
            fd[age] = sum(f == age for f in fish)
        
        for day in range(days):
            for age in range(9):
                fd[age - 1] = fd[age]
            fd[8] = fd[-1]
            fd[6] += fd[-1]
            fd[-1] = 0
        print(sum(fd[age] for age in range(9)))

if __name__ == "__main__":
    part_1(testing_file_name, 18)
    part_1(data_file_name, 80)
    part_2(testing_file_name, 256)
    part_2(data_file_name, 256)