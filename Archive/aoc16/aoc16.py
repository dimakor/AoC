import pathlib
import sys
from rich import print
import re

TEMPLATE = "Valve AA has flow rate=0; tunnels lead to valves DD, II, BB"
P1 = r"[A-Z][A-Z]"

def process(puzzle_input):
    """Parse input"""
    pressure = {}
    cave = {}
    for line in puzzle_input.split('\n'):
        v = line[6:8]
        a1 = line.find('=')
        a2 = line.find(';')
        m = line[a2+2:]
        leadto = m[m.find('valve'):].split()
        leadto.pop(0)
        cave[v] = leadto
        pressure[v] = line[a1+1:a2]
    print(pressure)
    print(cave)

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