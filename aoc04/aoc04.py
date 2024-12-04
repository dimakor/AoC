import pathlib
import sys
from rich import print
import re


def process(puzzle_input):
    """Parse input"""
    data = []
    for line in puzzle_input.split("\n"):
        data.append(line)
    return data


def findX(input_string):
    p = re.compile("XMAS")
    xm = p.findall(input_string)
    return len(xm)


def part1(data):
    """Solve part 1"""
    res = 0
    x = len(data[0])  # horizontal size
    y = len(data)  # vertical size
    # remember! data[y][x]
    for l in data:
        # plain horizontal search
        res += findX(l)
        # reverse horizontal search
        res += findX(l[::-1])
    # vertical search
    for i in range(x):
        vstring = "".join([data[j][i] for j in range(y)])
        res += findX(vstring)
        res += findX(vstring[::-1])  # reverse
    for i in range(x - 3):
        # main diagonal and up from it
        dstring = "".join([data[j][i + j] for j in range(y - i)])
        # print(dstring)
        # for j in range(y-i):
        #     print("X:", i+j)
        #     print("Y:", j)
        res += findX(dstring)
        res += findX(dstring[::-1])  # reverse
    for i in range(1, x - 3):
        # down from main diagonal
        dstring = "".join([data[j + i][j] for j in range(y - i)])
        res += findX(dstring)
        res += findX(dstring[::-1])  # reverse
    for i in range(x - 3):
        # other diagonal and up from it
        dstring = "".join([data[j][x - j - 1 - i] for j in range(x - i)])
        res += findX(dstring)
        res += findX(dstring[::-1])  # reverse
    for i in range(1, y - 3):
        # down from other diagonal
        dstring = "".join([data[i + j][x - j - 1] for j in range(x - i)])
        res += findX(dstring)
        res += findX(dstring[::-1])  # reverse
    return res


def part2(data):
    """Solve part 2"""
    res = 0
    x = len(data[0])  # horizontal size
    y = len(data)  # vertical size
    for j in range(y - 2):
        for i in range(x - 2):
            if data[j + 1][i + 1] != "A":
                continue
            cross = "".join([data[j][i], data[j + 2][i + 2]])
            if cross in ["MS", "SM"]:
                cross = "".join([data[j + 2][i], data[j][i + 2]])
                if cross in ["MS", "SM"]:
                    res += 1
    return res


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        data = process(puzzle_input)
        # solution1 = part1(data)
        solution2 = part2(data)
        # print("PART1:", solution1)
        print("PART2:", solution2)
