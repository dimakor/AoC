import pathlib
import sys
from rich import print
import parse
from collections import namedtuple
#from rich.progress import track
from tqdm import tqdm

TEMPLATE = "Sensor at x={:d}, y={:d}: closest beacon is at x={:d}, y={:d}"
Point = namedtuple("Point", "x y")

def mm(a : Point, b : Point):
    return abs(a.x - b.x) + abs(a.y - b.y)

def process(puzzle_input):
    """Parse input"""
    p = parse.compile(TEMPLATE)
    B = []
    S = []
    D = []
    for line in puzzle_input.split('\n'):
        r = p.parse(line)
        x = Point(r[0], r[1])
        y = Point(r[2], r[3])
        S.append(x)
        B.append(y)
        D.append(mm(x,y))
    return S, B, D

def find_interval(s, range, Y):
    # s - sensor we're intersecting with line Y
    prox = s.y-Y
    if abs(prox) > range:
        return None
    h = range - abs(prox)
    if (rx:=s.x+h) < 0:
        return None
    elif rx > 4000000:
        rx = 4000000
    if (lx:=s.x - h) > 4000000:
        return None
    elif lx < 0:
        lx = 0
    return [lx, rx]

def part1a(data):
    S = data[0]
    B = data[1]
    D = data[2]
    Y = 2000000
    #Y = 10
    points = [i.x for i in S] + [i.x for i in B]
    X = max(points)
    Xm = min(points)
    intervals = []
    for s, d in zip(S, D):
        if x:=find_interval(s, d, Y): 
            intervals.append(x)
    intervals.sort()
    stack = []
    stack.append(intervals[0])
    for interval in intervals[1:]:
        # Check for overlapping interval
        if stack[-1][0] <= interval[0] <= stack[-1][-1]:
            stack[-1][-1] = max(stack[-1][-1], interval[-1])
        else:
            stack.append(interval)
    points = sum(i[1] - i[0] +1 for i in stack)
    bic = sum(1 for b in set(B) if b.y == Y)
    return points-bic

def part2(data):
    """Solve part 2"""
    S = data[0]
    B = data[1]
    D = data[2]
    Y = 4000000
    #Y = 20
    X = Y
    SS = set(S+B)
    for y in tqdm(range(Y+1)):
    #for y in range(Y+1):
        intervals = []
        for s, d in zip(S, D):
            if x:=find_interval(s, d, y): 
                intervals.append(x)
        intervals.sort()
        stack = []
        stack.append(intervals[0])
        for interval in intervals[1:]:
        # Check for overlapping interval
            if stack[-1][0] <= interval[0] <= stack[-1][-1]:
                stack[-1][-1] = max(stack[-1][-1], interval[-1])
            else:
                stack.append(interval)
        if sum((s[1] - s[0]) for s in stack) == X:
            continue
        for point in range(X+1):
            if Point(point, y) in SS:
                continue
            for i in stack:
                if check_point(i, point):
                    break
            else:
                return point*4000000 + y
            

def check_point(interval, point):
    if interval[0] <= point <= interval[1]:
        return True
    else:
        return False

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        data = process(puzzle_input)
        # solution1 = part1a(data)
        solution2 = part2(data)
        # print("PART1:", solution1)
        print("PART2:", solution2)