# aoc06.py

import pathlib
import sys
from rich import print
from rich.pretty import pprint

def parse(puzzle_input):
    """Parse input"""
    f = [] # Forest
    for line in puzzle_input.split('\n'):
        f.append([int(i) for i in line])
    fsize = len(f[0])
    v =[[0 for _ in range(fsize)] for _ in range(fsize)]
    return f,v

def part1(f, v):
    """Solve part 1"""
    fsize = len(f[0])
    # left - right
    h = 0
    for i in range(fsize):
        for j in range(fsize):
            if j == 0:
                h = f[i][j]
                v[i][j] = 1
            elif h < f[i][j]:
                v[i][j] = 1
                h = f[i][j]
    # right - left
    h = 0
    for i in range(fsize):
        for j in range(fsize-1, 0, -1):
            if j == fsize - 1:
                h = f[i][j]
                v[i][j] = 1
            elif h < f[i][j]:
                v[i][j] = 1
                h = f[i][j]
    # bottom - up
    h = 0
    for i in range(fsize):
        for j in range(fsize-1, 0, -1):
            if j == fsize - 1:
                h = f[j][i]
                v[j][i] = 1
            elif h < f[j][i]:
                v[j][i] = 1
                h = f[j][i]
    # top - down
    h = 0
    for i in range(fsize):
        for j in range(fsize):
            if j == 0:
                h = f[j][i]
                v[j][i] = 1
            elif h < f[j][i]:
                v[j][i] = 1
                h = f[j][i]

    return sum([sum(i) for i in v])

def sc(f, x, y):
    fsize = len(f[0])
    # up
    total_sc = sc = 0
    for i in range(y-1, -1, -1):
        sc += 1
        if f[y][x] <= f[i][x]:
            break
    total_sc = sc
    # down
    sc = 0
    for i in range(y+1, fsize):
        sc += 1
        if f[y][x] <= f[i][x]:
            break
    total_sc *= sc
    # right
    sc = 0
    for i in range(x+1, fsize):
        sc += 1
        if f[y][x] <= f[y][i]:
            break
    total_sc *= sc
    # left
    sc = 0
    for i in range(x-1, -1, -1):
        sc += 1
        if f[y][x] <= f[y][i]:
            break
    total_sc *= sc
    return total_sc

def part2(f, v):
    """Solve part 2"""
    fsize = len(f[0])
    m = 0
    for i in range(1, fsize):
        for j in range(1, fsize):
            s = sc(f, i, j)
            if m<s:
                m = s
    return m

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    f, v = parse(puzzle_input)
    solution1 = part1(f, v)
    solution2 = part2(f, v)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))