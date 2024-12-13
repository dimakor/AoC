import pathlib
import sys
from rich import print
import parse

def process(puzzle_input):
    """Parse input"""
    buttontxt = parse.compile("Button {}: X+{}, Y+{}")
    prizetxt = parse.compile("Prize: X={}, Y={}")
    lines = puzzle_input.split('\n')
    A = []
    B = []
    PRIZE = []
    for i in range(0, len(lines), 4):
        res = buttontxt.parse(lines[i])
        A.append((int(res[1]), int(res[2])))
        res = buttontxt.parse(lines[i+1])
        B.append((int(res[1]), int(res[2])))
        res = prizetxt.parse(lines[i+2])
        PRIZE.append((int(res[0]), int(res[1])))
    return A, B, PRIZE
        
def bounds(a, b , prize):
    maxax = int((prize[0] - b[0]) / a[0])
    maxay = int((prize[1] - b[1]) / a[1])
    maxbx = int((prize[0] - a[0]) / b[0])
    maxby = int((prize[1] - a[1]) / b[1])
    return min(maxax, maxay), min(maxbx, maxby)


def part1(data):
    """Solve part 1"""
    A, B, PRIZE = data
    total = len(A)
    e = 0
    result = 0
    for a, b, pr in zip(A, B, PRIZE):
        e += 1
        tokens = 1000000
        print(e, " of ", total)
        maxa, maxb = 100, 100 #bounds(a, b, pr)
        for i in range(1, maxa):
            for j in range(1, maxb):
                if (i*a[0] + j*b[0]) != pr[0] or (i*a[1] + j*b[1]) != pr[1]:
                    continue
                t = i*3 + j 
                if t < tokens:
                    tokens = t
        if tokens != 1000000:
            result += tokens
    return result

def calc(a, b, pr):
    m = (pr[1] *a [0] - a[1]* pr[0]) / (b[1] * a[0] - b[0] *a[1])
    n = (pr[0] - b[0] * m) / a[0]
    mi = int(m)
    ni = int(n)
    if (m - mi != 0) or (n - ni != 0):
        return 0,0
    return ni, mi

def part2(data):
    """Solve part 2"""
    A, B, PRIZE = data
    total = len(A)
    e = 0
    result = 0
    for a, b, pr in zip(A, B, PRIZE):
        e += 1
        prnew = (pr[0] + 10000000000000, pr[1] + 10000000000000)
        print(e, " of ", total)
        n, m = calc(a,b, prnew)
        if n == 0:
            continue
        result += 3* n + m
    return result

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        data = process(puzzle_input)
        #solution1 = part1(data)
        solution2 = part2(data)
        #print("PART1:", solution1)
        print("PART2:", solution2)