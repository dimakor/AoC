# aoc202201.py

import pathlib
import sys

def parse(puzzle_input):
    """Parse input"""
    acc = 0
    result = list()
    for line in puzzle_input.split('\n'):
        if not line:
            result.append(acc)
            acc = 0
            continue
        acc += int(line)
    result.append(acc)
    return result

def part1(data):
    """Solve part 1"""
    return max(data)


def part2(data):
    """Solve part 2"""
    data.sort(reverse=True)
    return data[0]+data[1]+data[2]

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