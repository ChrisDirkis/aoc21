from itertools import *
from functools import *
from math import * 
import re
from collections import defaultdict 

from typing import *

data_file_name = "inputs/day4"
testing_file_name = data_file_name + "_test"

def parse_file(file):
    text = file.read()
    segments = text.split("\n\n")
    sequence = [int(v) for v in segments[0].split(",")]
    boards = []
    for board_text in segments[1:]:
        board = []
        for line in board_text.split("\n"):
            board.append([int(v) for v in line.split(" ") if v])
        boards.append(board)
    return sequence, boards

def check_board(sequence, board):
    for line in board:
        if all(v in sequence for v in line):
            return True
    for i in range(len(board[0])):
        column = [line[i] for line in board]
        if all(v in sequence for v in column):
            return True

    return False

def score_board(sequence, board):
    board_sum = 0
    for line in board:
        for v in line:
            if v not in sequence:
                board_sum += v
    board_sum *= sequence[-1]
    return board_sum

def part_1(filename):
    print(f"Part 1: {filename}")
    with open(filename) as file:
        seq, boards = parse_file(file)
        for i in range(1, len(seq)):
            subseq = seq[:i]
            for board in boards:
                if check_board(subseq, board):
                    print(score_board(subseq, board))
                    return

def part_2(filename):
    print(f"Part 2: {filename}")
    with open(filename) as file:
        seq, boards = parse_file(file)
        for i in range(1, len(seq)):
            subseq = seq[:i]
            to_remove = []
            for board in boards:
                if check_board(subseq, board):
                    if len(boards) == 1:
                        print(score_board(subseq, board))
                        return
                    else:
                        to_remove.append(board)
            for board in to_remove:
                boards.remove(board)

if __name__ == "__main__":
    part_1(testing_file_name)
    part_1(data_file_name)
    part_2(testing_file_name)
    part_2(data_file_name)