import pathlib
import sys
from rich import print
import math
from itertools import product, count


def process(puzzle_input):
    """Parse input"""
    connections = dict()
    hist = set()
    vertices = set()
    for line in puzzle_input.split("\n"):
        c1 = line[0:2]
        c2 = line[3:5]
        vertices.add(c1)
        vertices.add(c2)
        try:
            connections[c1].add(c2)
        except KeyError:
            connections[c1] = {c2}
        try:
            connections[c2].add(c1)
        except KeyError:
            connections[c2] = {c1}
        if c1[0] == "t":
            hist.add(c1)
        if c2[0] == "t":
            hist.add(c2)

    return connections, hist, vertices


def part1(data):
    """Solve part 1"""
    connections, hist, _ = data
    t = set(
        tuple(sorted((x, y, z)))
        for x in connections
        for y in connections[x]
        for z in connections[y]
        if x in connections[z]
    )
    return sum(x[0] == "t" or y[0] == "t" or z[0] == "t" for x, y, z in t)

def BronKerbosch1(R, P, X, connections, C):
    if len(P) == 0 and len(X) == 0:
        C.append(R)
        return
    pp = set(P)
    while pp:
        v = pp.pop()
        BronKerbosch1(R | {v}, pp & set(connections[v]), X & set(connections[v]), connections, C)
        X = X | {v}

def BronKerbosch2(R, P, X, c):
    P = set(P)
    if not P and not X:
        yield R
    while P:
        v = P.pop()
        yield from BronKerbosch2(R.union([v]),
            P.intersection(c[v]), X.intersection(c[v]), c)
        X.add(v)

def part2(data):
    """Solve part 2"""
    connections, hist, vertices = data
    R = set()
    X = set()
    C = []
    BronKerbosch1(R, vertices, X, connections, C)
    # C = list(BronKerbosch2(R, vertices, X, connections))
    code = sorted(max(C, key=len))
    jcode = [c + ',' for c in code]       
    return ''.join(jcode)

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        data = process(puzzle_input)
        solution1 = part1(data)
        solution2 = part2(data)
        print("PART1:", solution1)
        print("PART2:", solution2)
