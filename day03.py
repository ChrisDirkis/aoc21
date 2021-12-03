from itertools import *
from functools import *
from math import * 
import re
from collections import defaultdict 

from typing import *

data_file_name = "inputs/day3"
testing_file_name = data_file_name + "_test"

def part_1(filename):
    print(f"Part 1: {filename}")
    with open(filename) as file:
        strs = [line for line in file]
        bit_len = len(strs[0]) - 1
        bits = [0] * bit_len
        for i in range(bit_len):
            bits[i] = "1" if sum(line[i] == "1" for line in strs) > len(strs) / 2 else "0"
        gamma_str = "".join(bits)
        gamma = int(gamma_str, 2)
        eps_str = "".join("0" if c == "1" else "1" for c in gamma_str)
        eps = int(eps_str, 2)
        print(gamma, eps, gamma * eps)


def part_2(filename):
    print(f"Part 2: {filename}")
    with open(filename) as file:
        strs = [line for line in file]
        bit_len = len(strs[0]) - 1

        gamma = 0
        gamma_strs = strs
        bits = [0] * bit_len
        for i in range(bit_len):
            ones = sum(line[i] == "1" for line in gamma_strs)
            if ones == len(gamma_strs) / 2:
                bits[i] = "1"
            else:
                bits[i] = "1" if ones > len(gamma_strs) / 2 else "0"
            print(f"the most common bit in pos {i} is {bits[i]}")
            gamma_strs = [s for s in gamma_strs if s[i] == bits[i]]

            print(gamma_strs)
            if len(gamma_strs) == 1:
                gamma = int(gamma_strs[0], 2)
                print("gamma is", gamma, gamma_strs[0])
                break
        

        eps = 0
        eps_strs = strs
        bits = [0] * bit_len
        for i in range(bit_len):
            
            ones = sum(line[i] == "1" for line in eps_strs)
            if ones == len(eps_strs) / 2:
                bits[i] = "0"
            else:
                bits[i] = "0" if ones > len(eps_strs) / 2 else "1"
            print(f"the least common bit in pos {i} is {bits[i]}")
            eps_strs = [s for s in eps_strs if s[i] == bits[i]]
            if len(eps_strs) == 1:
                eps = int(eps_strs[0], 2)
                print("epsilon is", eps, eps_strs[0])
                break

        print(gamma * eps)
if __name__ == "__main__":
    part_1(testing_file_name)
    part_1(data_file_name)
    part_2(testing_file_name)
    part_2(data_file_name)