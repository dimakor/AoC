# aoc202203.py

import pathlib
import sys
from rich import print

def parse1(puzzle_input):
    """Parse input"""
    #print("a:", ord('a'), "  z:", ord('z'))
    #print("A:", ord('A'), "  Z:", ord('Z'))

    sum = 0
    for line in puzzle_input.split('\n'):
        l = len(line)
        comp1 = set(line[0: l//2])
        comp2 = set(line[l//2:])
        letter = comp1.intersection(comp2).pop()
        if letter.islower():
            sum += ord(letter) - 96
        else:
            sum += ord(letter) - 38
    print("SUM:", sum)
    return [ line for line in puzzle_input.split('\n')]

def parse2(puzzle_input):
    """Parse input"""
    #print("a:", ord('a'), "  z:", ord('z'))
    #print("A:", ord('A'), "  Z:", ord('Z'))

    sum = 0
    inp = puzzle_input.split('\n')
    for i in range(0, len(inp), 3):
        comp1 = set(inp[i])
        letter = comp1.intersection(inp[i+1]).intersection(inp[i+2]).pop()
        if letter.islower():
            sum += ord(letter) - 96
        else:
            sum += ord(letter) - 38
    print("SUM:", sum)
    return [ line for line in puzzle_input.split('\n')]

def part1(data):
    """Solve part 1"""

def part2(data):
    """Solve part 2"""

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse2(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))