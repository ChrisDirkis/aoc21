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

def part_1(filename, template: str):
    print(f"Part 1: {filename}")
    with open(filename) as file:
        lines = [line.strip().split(" -> ") for line in file]
        rules = dict()
        for pair, insert in lines:
            rules[pair] = insert
        
        for _ in range(10):
            insertions = []
            for i, (a, b) in enumerate(zip(template, template[1:])):
                if a + b in rules:
                    insertions.append((rules[a + b], i))
            #print(insertions)
            o = 0
            for s, i in insertions:
                template = template[:i+o+1] + s + template[i+o+1:]
                o += 1
            #print(template)
        
        letters = set(template)
        counts = sorted((template.count(letter), letter) for letter in letters)
        print(counts)
        print(counts[-1][0] - counts[0][0])
        pass

def part_2(filename, template):
    print(f"Part 2: {filename}")
    with open(filename) as file:
        lines = [line.strip().split(" -> ") for line in file]
        rules = dict()
        for pair, insert in lines:
            rules[pair] = insert
        
        t = defaultdict(lambda: 0)
        for pair in zip(template, template[1:]):
            t[pair[0] + pair[1]] += 1
        
        for _ in range(40):
            #print(t)
            nt = defaultdict(lambda: 0)
            for pair in t.keys():
                pc = t[pair]
                #print(pair, pc)
                if pair in rules:
                    nt[pair[0] + rules[pair]] += pc
                    nt[rules[pair] + pair[1]] += pc
            t = nt
        letters = set()
        for key in t.keys():
            letters.add(key[0])
            letters.add(key[1])


        counts = dict()
        for letter in letters:
            starts = sum(t[k] for k in t.keys() if k[0] == letter)
            ends = sum(t[k] for k in t.keys() if k[1] == letter)
            counts[letter] = starts + abs(starts - ends)
        print(counts)

        c = sorted((counts[v], v) for v in counts)
        print(c)
        print(c[-1][0] - c[0][0])
        #print([(pair, t[pair]) for pair in t.keys()])

if __name__ == "__main__":
    part_1(testing_file_name, "NNCB")
    part_1(data_file_name, "VCOPVNKPFOOVPVSBKCOF")
    part_2(testing_file_name, "NNCB")
    part_2(data_file_name, "VCOPVNKPFOOVPVSBKCOF")