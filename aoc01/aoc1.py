import pathlib
import sys
from rich import print

def process(puzzle_input):
    """Parse input"""
    data1 = []
    data2 = []
    for line in puzzle_input.split('\n'):
        r = line.split()
        data1.append(int(r[0]))
        data2.append(int(r[1]))
    return (data1, data2)


def part1(data):
    """Solve part 1"""
    data[0].sort()
    data[1].sort()
    sol = sum(abs(data[0][i]-data[1][i]) for i in range(len(data[0])))
    return sol

def part2(data):
    """Solve part 2"""
    score = 0
    d1 = data[0]
    d2 = data[1]
    for i in d1:
        score += i*d2.count(i)
    return score

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        data = process(puzzle_input)
        solution1 = part1(data)
        solution2 = part2(data)
        print("PART1:", solution1)
        print("PART2:", solution2)