from itertools import *
from functools import *
from math import * 
import re
from collections import defaultdict 

from typing import *

data_file_name = "inputs/day8"
testing_file_name = data_file_name + "_test"

def part_1(filename):
    print(f"Part 1: {filename}")
    with open(filename) as file:
        outputs = [line.strip().split(" | ")[1].split(" ") for line in file]
        unique = {2, 4, 3, 7}
        print(sum(sum(len(o) in unique for o in output) for output in outputs))

def part_2(filename):
    print(f"Part 2: {filename}")
    with open(filename) as file:
        values = [[v.split(" ") for v in line.strip().split(" | ")] for line in file]
        #print(values)

        s = 0
        perms = list(permutations("abcdefg"))
        vals = [
            "abcefg",
            "cf",
            "acdeg",
            "acdfg",
            "bcdf",
            "abdfg",
            "abdefg",
            "acf",
            "abcdefg",
            "abcdfg",
        ]
        oa = ord("a")
        valset = set(vals)
        print(valset)
        for line in values:
            i = line[0]
            o = line[1]
            nums = i + o

            for perm in perms:
                permed = ("".join(sorted(perm[ord(c) - oa] for c in v)) for v in nums)
                if all(p in valset for p in permed):
                    out = ["".join(sorted(perm[ord(c) - oa] for c in v)) for v in nums][-4:]
                    val = sum(10**(3-i) * vals.index(out[i]) for i in range(4))
                    print(out, val)
                    s += val
                    break
        print(s)
                    
                
            
                
        pass

if __name__ == "__main__":
    part_1(testing_file_name)
    part_1(data_file_name)
    part_2(testing_file_name)
    part_2(data_file_name)