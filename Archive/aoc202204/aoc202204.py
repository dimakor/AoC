# aoc202204.py

import pathlib
import sys
from rich import print

def parse1(puzzle_input):
    """Parse input"""
    sum = 0
    for line in puzzle_input.split('\n'):
        areas = []
        for area in line.split(','):
            a = area.split('-')
            areas.append(int(a[0]))
            areas.append(int(a[1]))
        if ((areas[0] >= areas[2] and areas[1] <= areas[3]) or
            (areas[0] <= areas[2] and areas[1] >= areas[3])):
            sum += 1

    print("PART1:", sum)
    return [ line for line in puzzle_input.split('\n')]

def parse2(puzzle_input):
    """Parse input"""
    sum = 0
    for line in puzzle_input.split('\n'):
        areas = []
        for area in line.split(','):
            a = area.split('-')
            areas.append(int(a[0]))
            areas.append(int(a[1]))
        if ((areas[0] <= areas[3] and areas[1] >= areas[2]) or
            (areas[2] <= areas[1] and areas[3] >= areas[0])):
            sum += 1

    print("PART2:", sum)

def part1(data):
    """Solve part 1"""

def part2(data):
    """Solve part 2"""

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse1(puzzle_input)
    parse2(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))