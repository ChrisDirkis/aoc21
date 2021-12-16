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

def parse_packet(pbs, start):
    version = int(pbs[start:start+3], base=2)
    type = int(pbs[start+3:start+6], base=2)
    #print(start, version)
    if type == 4:
        sb = ""
        i = 0
        while True:
            sb += pbs[start+6 + i * 5 + 1:start+6 + i * 5 + 5]
            if pbs[start+6 + i * 5] == "0":
                break 
            i += 1
        packet_len = 6 + i * 5 + 5
        value = int(sb, base=2)
        return (version, type, packet_len, value)
    else:
        ltype = pbs[start+6]
        if ltype == "0":
            #sub packet length in bits, 15 bits
            spl = int(pbs[start+7:start+7+15], base=2)
            #print("spl", spl)
            ps = []
            ul = 0
            while True:
                packet = parse_packet(pbs, start + 7 + 15 + ul)
                ul += packet[2]
                ps.append(packet)
                if ul == spl:
                    break
            return (version, type, spl + 6 + 1 + 15, ps)
        else:
            # sub packet count, 11 bits
            spc = int(pbs[start+7:start+7+11], base=2)
            #print("spc", spc)
            ps = []
            ul = 0
            for _ in range(spc):
                packet = parse_packet(pbs, start + 7 + 11 + ul)
                ul += packet[2]
                ps.append(packet)
            return (version, type, ul + 6 + 1 + 11, ps)


def part_1(filename):
    print(f"Part 1: {filename}")
    with open(filename) as file:
        bys = [int(v, base=16) for v in file.read().strip()]
        bs = "".join((4 - len(f"{v:b}")) * "0" + f"{v:b}" for v in bys)
        #print(bs)
        packet = parse_packet(bs, 0)
        s = 0
        frontier = [packet]
        while frontier:
            p = frontier.pop()
            s += p[0]
            if isinstance(p[3], list):
                for sp in p[3]:
                    frontier.append(sp)
        print(s)

def value(packet):
    if packet[1] == 4:
        return packet[3]

    elif packet[1] == 0:
        return sum(value(p) for p in packet[3])
    elif packet[1] == 1:
        return prod(value(p) for p in packet[3])
    elif packet[1] == 2:
        return min(value(p) for p in packet[3])
    elif packet[1] == 3:
        return max(value(p) for p in packet[3])

    elif packet[1] == 5:
        return 1 if value(packet[3][0]) > value(packet[3][1]) else 0
    elif packet[1] == 6:
        return 1 if value(packet[3][0]) < value(packet[3][1]) else 0
    elif packet[1] == 7:
        return 1 if value(packet[3][0]) == value(packet[3][1]) else 0


def part_2(filename):
    print(f"Part 2: {filename}")
    with open(filename) as file:
        bys = [int(v, base=16) for v in file.read().strip()]
        bs = "".join((4 - len(f"{v:b}")) * "0" + f"{v:b}" for v in bys)
        #print(bs)
        packet = parse_packet(bs, 0)
        print(value(packet))

if __name__ == "__main__":
    part_1(testing_file_name)
    part_1(data_file_name)
    part_2(testing_file_name)
    part_2(data_file_name)