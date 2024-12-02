import pathlib
import sys
from rich import print
import parse

def process(puzzle_input):
    """Parse input"""
    data = []
    for line in puzzle_input.split('\n'):
        data.append([int(i) for i in line.split()])
    return data
        
def is_safe(report):
    if report[0] < report[1]:
        # incr
        for i in range(0, len(report)-1):
            if 0 < report[i+1] - report[i] < 4:
                continue
            else:
                return False
    elif report[0] > report[1]:
        # decr
        for i in range(0, len(report)-1):
            if 0 < report[i] - report[i+1] < 4:
                continue
            else:
                return False
    else:
        return False
    return True

def is_safe2(report):
    if is_safe(report):
        return True
    for i in range(len(report)):
        rep2 = report.copy()
        rep2.pop(i)
        if is_safe(rep2):
            return True
    return False


def part1(data):
    """Solve part 1"""
    res = 0
    for report in data:
        if is_safe(report):
            res += 1
    return res


def part2(data):
    """Solve part 2"""
    res = 0
    for report in data:
        if is_safe2(report):
            res += 1
    return res

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        data = process(puzzle_input)
        solution1 = part1(data)
        solution2 = part2(data)
        print("PART1:", solution1)
        print("PART2:", solution2)