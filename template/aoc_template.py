import pathlib
import sys
from rich import print
import parse

def process(puzzle_input):
    """Parse input"""
    for line in puzzle_input.split('\n'):
        

def part1(data):
    """Solve part 1"""

def part2(data):
    """Solve part 2"""

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        data = process(puzzle_input)
        solution1 = part1(data)
        solution2 = part2(data)
        print("PART1:", solution1)
        print("PART2:", solution2)