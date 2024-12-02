# aoc_template.py for Advent of Code

import pathlib
import sys
from rich import print


def parse(puzzle_input):
    """Parse input"""
    return puzzle_input

def part1(data):
    """Solve part 1"""
    for i in range(3, len(data)+1):
        buf = set([data[j] for j in range(i-3, i+1)])
        #print("I:",i, "BUF:", buf)
        if len(buf) == 4:
            return i+1

def part2(data):
    """Solve part 2"""
    for i in range(13, len(data)+1):
        buf = set([data[j] for j in range(i-13, i+1)])
        #print("I:",i, "BUF:", buf)
        if len(buf) == 14:
            return i+1

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))