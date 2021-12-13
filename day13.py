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

def print_dots(dots):
    max_x = max(x for x, y in dots) + 1
    max_y = max(y for x, y in dots) + 1
    grid = gen_grid((max_x, max_y))
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            grid[x][y] = "#" if vec2(x, y) in dots else "."
    for line in grid:
        print(line)

def part_1(filename):
    print(f"Part 1: {filename}")
    with open(filename) as file:
        lists = [s.split("\n") for s in file.read().split("\n\n")]
        dots_s = lists[0]

        dots = [vec2(int(v.split(",")[0]), int(v.split(",")[1])) for v in dots_s]
        dd = set()
        for dot in dots:
            dd.add(dot)

        print(len(dd))
        #print_dots(dd)
        
        folds = [(v.split("=")[0], int(v.split("=")[1])) for v in lists[1]]

        for fold in folds:
            to_remove = []
            to_add = []
            if fold[0] == "y":
                for dot in dd:
                    if dot.y > fold[1]:
                        to_remove.append(dot)
                        to_add.append((dot.x, fold[1] * 2 - dot.y))
            
            else:
                for dot in dd:
                    if dot.x > fold[1]:
                        to_remove.append(dot)
                        to_add.append((fold[1] * 2 - dot.x, dot.y))

            for dot in to_remove:
                #print(f"removing {dot}")
                dd.remove(dot)
            for dot in to_add:
                if dot not in dd:
                    #print(f"adding {dot}")
                    dd.add(vec2(*dot))


            print(len(dd))
            
            #print_dots(dd)
            return


def part_2(filename):
    print(f"Part 2: {filename}")
    with open(filename) as file:    
        lists = [s.split("\n") for s in file.read().split("\n\n")]
        dots_s = lists[0]

        dots = [vec2(int(v.split(",")[0]), int(v.split(",")[1])) for v in dots_s]
        dd = set()
        for dot in dots:
            dd.add(dot)

        print(len(dd))
        #print_dots(dd)
        
        folds = [(v.split("=")[0], int(v.split("=")[1])) for v in lists[1]]

        for fold in folds:
            to_remove = []
            to_add = []
            if fold[0] == "y":
                for dot in dd:
                    if dot.y > fold[1]:
                        to_remove.append(dot)
                        to_add.append((dot.x, fold[1] * 2 - dot.y))
            
            else:
                for dot in dd:
                    if dot.x > fold[1]:
                        to_remove.append(dot)
                        to_add.append((fold[1] * 2 - dot.x, dot.y))

            for dot in to_remove:
                #print(f"removing {dot}")
                dd.remove(dot)
            for dot in to_add:
                if dot not in dd:
                    #print(f"adding {dot}")
                    dd.add(vec2(*dot))


            print(len(dd))
        print_dots(dd)
        print(dd)

if __name__ == "__main__":
    part_1(testing_file_name)
    part_1(data_file_name)
    part_2(testing_file_name)
    part_2(data_file_name)