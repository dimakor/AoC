# aoc201901.py

import pathlib
import sys

def parse(puzzle_input):
    """Parse input"""
    return [int(line) for line in puzzle_input.split()]

def part1(data):
    """Solve part 1"""
    total = 0
    for i in data:
        total += i // 3 - 2
    return total

def modfuel(mod):
    ''' Calculate fuel necessary for given module mass'''
    fmass = mod // 3 - 2
    if fmass > 0:
        return fmass + modfuel(fmass)
    else:
        return 0

def part2(data):
    """Solve part 2"""
    total = totalf = 0
    for i in data:
        fmass = i // 3 - 2
        total += fmass
        totalf += modfuel(fmass)
    return total + totalf

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