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
        lines = [digit_re.findall(line) for line in file]
        pass

def part_2(filename):
    print(f"Part 2: {filename}")
    with open(filename) as file:
        lines = [digit_re.findall(line) for line in file]
        pass

if __name__ == "__main__":
    part_1(testing_file_name)
    part_1(data_file_name)
    part_2(testing_file_name)
    part_2(data_file_name)