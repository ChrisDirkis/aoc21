from itertools import *
from functools import *
from math import * 
import re
from collections import defaultdict

from grid import *

import heapq

digit_re = re.compile(r"(\d+)")

aod_day = str(int(__file__.split("/")[-1][3:5]))
data_file_name = "inputs/day" + aod_day
testing_file_name = data_file_name + "_test"

def part_1(filename):
    print(f"Part 1: {filename}")
    with open(filename) as file:
        lines = [[int(v) for v in line.strip()] for line in file]
        dims = vec2(len(lines[0]), len(lines))
        end = sub_t(dims, (1, 1))


        seen = set()
        seen.add(vec2(0, 0))
        heap = [(0, [vec2(0, 0)])]
        while True:
            v, ps = heapq.heappop(heap)
            ns = adj(ps[-1], dims)
            for n in ns:
                
                if n == end:
                    for p in ps:
                        #print(p, lines[p.y][p.x])
                        pass
                    print(v + lines[n.y][n.x])
                    return
                if n not in seen:
                    try:
                        heapq.heappush(heap, (v + lines[n.y][n.x], ps + [n]))
                    except:
                        pass
                        #print(n)
                    seen.add(n)

        pass

def part_2(filename):
    print(f"Part 2: {filename}")
    with open(filename) as file:
        lines = [[int(v) for v in line.strip()] for line in file]
        dims = vec2(len(lines[0]), len(lines))

        ol = lines
        od = dims
        dims = dot_t(dims, (5, 5))

        lines = [[0] * dims.x for _ in range(dims.y)]
        for i, j in product(range(5), repeat=2):
            for x, y in product(range(od.x), range(od.y)):
                lines[y + od.y * j][x + od.x * i] = ((ol[y][x] - 1 + i + j) % 9) + 1 

        print(lines[0])
        end = sub_t(dims, (1, 1))


        seen = set()
        seen.add(vec2(0, 0))
        heap = [(0, [vec2(0, 0)])]
        while True:
            v, ps = heapq.heappop(heap)
            ns = adj(ps[-1], dims)
            for n in ns:
                
                if n == end:
                    for p in ps:
                        #print(p, lines[p.y][p.x])
                        pass
                    print(v + lines[n.y][n.x])
                    return
                if n not in seen:
                    try:
                        heapq.heappush(heap, (v + lines[n.y][n.x], ps + [n]))
                    except:
                        pass
                        #print(n)
                    seen.add(n)
        pass

if __name__ == "__main__":
    part_1(testing_file_name)
    part_1(data_file_name)
    part_2(testing_file_name)
    part_2(data_file_name)