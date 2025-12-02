import pathlib
import sys
from rich import print
#import parse
import re

def process(puzzle_input):
    """Parse input"""
    return puzzle_input
        

def part1(data):
    """Solve part 1"""
    p = re.compile('mul\((\d+),(\d+)\)')
    muls = p.findall(data)

    res = 0
    for mul in muls:
        res += int(mul[0])*int(mul[1])
    return res

def part2(data):
    """Solve part 2"""
    p = re.compile('do\(\)')
    dos = p.split(data)
    dn = re.compile('don\'t\(\)')
    p = re.compile('mul\((\d+),(\d+)\)')
    res = 0
    for d in dos:
        do = dn.split(d)
        muls = p.findall(do[0])
        for mul in muls:
            res += int(mul[0])*int(mul[1])
    return res

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text()#.strip()
        data = process(puzzle_input)
        solution1 = part1(data)
        solution2 = part2(data)
        print("PART1:", solution1)
        print("PART2:", solution2)