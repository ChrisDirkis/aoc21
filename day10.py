from itertools import *
from functools import *
from math import * 
import re
from collections import defaultdict 

from typing import *

digit_re = re.compile(r"(\d+)")

data_file_name = "inputs/day10"
testing_file_name = data_file_name + "_test"

costs = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}
costs2 = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
}

openers = {"(", "[", "{", "<"}
pairs = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}
def find_break(line):
    stack = []
    for v in line:
        if v in openers:
            stack.append(v)
        else:
            if (not stack) or v != pairs[stack[-1]]:
                return v
            else:
                stack.pop()

    return None 
            

def close_score(line):
    stack = []
    for v in line:
        if v in openers:
            stack.append(v)
        else:
            stack.pop()

    if not stack:
        return 0
    s = 0
    print(stack)
    for v in reversed(stack):
        print(v)
        s *= 5
        s += costs2[v]
        print(s)
    return s


def part_1(filename):
    print(f"Part 1: {filename}")
    with open(filename) as file:
        print(sum(costs[find_break(line.strip())] for line in file if find_break(line.strip())))


def part_2(filename):
    print(f"Part 2: {filename}")
    with open(filename) as file:
        lines = [line.strip() for line in file if not find_break(line.strip())]
        scores = sorted(close_score(line) for line in lines)
        print(scores)
        print(scores[len(scores) // 2])

if __name__ == "__main__":
    part_1(testing_file_name)
    part_1(data_file_name)
    part_2(testing_file_name)
    part_2(data_file_name)