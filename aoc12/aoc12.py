import pathlib
import sys
from rich import print
import itertools


def process(puzzle_input):
    """Parse input"""
    field = []
    for line in puzzle_input.split("\n"):
        field.append(list(line))
    # print(field)
    return field


def find_area(data, c, cy, cx, visited, sides):
    mx = len(data[0])
    my = len(data)
    if (cy < 0) or (cx < 0) or (cy >= my) or (cx >= mx):
        return 0, 1
    if data[cy][cx] != c:
        return 0, 1
    if (cy, cx) in visited:
        return 0, 0
    visited.add((cy, cx))
    area = 1
    fences = 0
    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        a, f = find_area(data, c, cy + dy, cx + dx, visited, sides)
        if a == 0 and f == 1:
            sides.append([(cy, cx), (dy, dx)])
        area += a
        fences += f
    return area, fences


def isout(y, x, my, mx):
    if (0 <= y < my) and (0 <= x < mx):
        return False
    return True


def find_sides(data, c, cy, cx):
    mx = len(data[0])
    my = len(data)
    idy = dy = 0
    idx = dx = 1
    corner = 1
    sx = cx
    sy = cy
    it = 1
    while ((sx != cx) or (sy != cy)) or it == 1:
        it = 0
        if isout(sy + dy, sx + dx, my, mx) or data[sy + dy][sx + dx] != c:
            cwx = -dy
            cwy = dx
            if not isout(sy + cwy, sx + cwx, my, mx):
                corner += 1
                dx = cwx
                dy = cwy
                if data[sy + cwy][sx + cwx] != c:
                    dx, dy = -dy, dx
                    corner += 1
        sy += dy
        sx += dx
        ccwx = dy
        ccwy = -dx
        if isout(sy + ccwy, sx + ccwx, my, mx):
            continue
        if data[sy + ccwy][sx + ccwx] == c:
            dy = ccwy
            dx = ccwx
            corner += 1
    if dx == -idx and dy == -idy:
        corner += 1
    return corner


def part1(data):
    """Solve part 1"""
    fences = 0
    mx = len(data[0])
    my = len(data)
    area = []
    visited = set()
    for y, row in enumerate(data):
        for x, c in enumerate(row):
            fences = 0
            sides = []
            a, f = find_area(data, c, y, x, visited, sides)
            if a != 0:
                area.append((c, a, f, sides.copy()))
    cost = 0
    cost2 = 0
    for c, a, f, sides in area:
        cost += a * f
        cost2 += a * calc_sides(sides)
    return cost, cost2


def calc_sides(sides):
    total = len(sides)
    for a, b in itertools.combinations(sides, 2):
        if (abs(a[0][0] - b[0][0]) == 1 and a[0][1] - b[0][1] == 0) or (
                    abs(a[0][1] - b[0][1]) == 1 and a[0][0] - b[0][0] == 0
                ):
            total -= 1
    return total


def part2(data):
    """Solve part 2"""
    print(find_sides(data, data[0][0], 0, 0))
    print(find_sides(data, data[1][0], 1, 0))


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        data = process(puzzle_input)
        solution1, solution2 = part1(data)
        # solution2 = part2(data)
        print("PART1:", solution1)
        print("PART2:", solution2)
