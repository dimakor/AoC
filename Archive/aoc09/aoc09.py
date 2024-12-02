# aoc06.py

import pathlib
import sys
from rich import print
import numpy as np

MOVE = {'R' : [1, 0],
        'L' : [-1, 0],
        'U' : [0, 1],
        'D' : [0, -1]}

def parse(puzzle_input):
    """Parse input"""
    H = [0, 0]
    T = [0, 0]
    size = 0
    mm = []
    mm.append(T)
    for line in puzzle_input.split('\n'):
        for i in range(int(line[2:])):
            H = move(H, MOVE[line[0]])
            T = move_tail(H, T)
            #size = max(size, T[0], T[1])
            if T not in mm:
                mm.append(T)
    return mm
            
def move(H, M):
    return [H[0] + M[0], H[1] + M[1]]

def move_tail(H, T):
    x = H[0] - T[0]
    y = H[1] - T[1]
    #print("X:", x, "  Y:", y)
    if abs(x) <=1 and abs(y) <=1:
        return T
    x = x//2 if abs(x)==2 else x
    y = y//2 if abs(y)==2 else y
    return [T[0] + x, T[1] +y]

def part1(data):
    """Solve part 1"""
    return len(data)

def part2(puzzle_input):
    """Solve part 2"""
    R = [ [0, 0] for _ in range(10) ]
    mm = []
    mm.append(R[9])
    for line in puzzle_input.split('\n'):
        for i in range(int(line[2:])):
            R[0] = move(R[0], MOVE[line[0]])
            for i in range(1,10):
                R[i] = move_tail(R[i-1], R[i])
            #size = max(size, T[0], T[1])
            if R[9] not in mm:
                mm.append(R[9])
    return len(mm)

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    #data = parse(puzzle_input)
    solution1 = part1(puzzle_input)
    solution2 = part2(puzzle_input)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))