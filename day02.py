from itertools import *
from functools import *
from math import * 
import re
from collections import defaultdict 

from typing import *

data_file_name = "inputs/day2"
testing_file_name = data_file_name + "_test"

def get_steps(file):
    steps = []
    for line in file:
        distance = int(line.split(" ")[1])
        direction_word = line.split(" ")[0]
        starting_letter = direction_word[0]
        
        if starting_letter == "f":
            steps.append((distance, 0))
        elif starting_letter == "d":
            steps.append((0, distance))
        elif starting_letter == "u":
            steps.append((0, -distance))
    return steps 

def part_1(filename):
    print(f"Part 1: {filename}")
    with open(filename) as file:
        steps = get_steps(file)
        forward_sum = sum(f for f, d in steps)
        downward_sum = sum(d for f, d in steps)
        print(forward_sum * downward_sum)

        

def part_2(filename):
    print(f"Part 2: {filename}")
    with open(filename) as file:
        steps = get_steps(file)
        aim = 0
        pos = (0, 0)
        print(pos)
        for step in steps:
            # if down or up
            if step[1] != 0:
                #pos = (pos[0], pos[1] + step[1])
                aim += step[1]
                # print("step", step)
                # print("aim", aim)
                # print(pos)
            # forward
            else:
                pos = (pos[0] + step[0], pos[1] + step[0] * aim)
                # print("step", step)
                # print("aim", aim)
                # print(pos)
        print(pos)
        print(pos[0] * pos[1])

if __name__ == "__main__":
    part_1(testing_file_name)
    part_1(data_file_name)
    part_2(testing_file_name)
    part_2(data_file_name)