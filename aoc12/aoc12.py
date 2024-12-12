import pathlib
import sys
from rich import print


def process(puzzle_input):
    """Parse input"""
    field = []
    for line in puzzle_input.split("\n"):
        field.append(list(line))
    # print(field)
    return field


def find_area(data, c, cy, cx, visited):
    mx = len(data[0])
    my = len(data)
    if (cy < 0) or (cx < 0) or (cy >= my) or (cx >= mx):
        return 0, 1
    if data[cy][cx] != c:
        return 0, 1
    if ((cy, cx) in visited):
        return 0, 0
    visited.add((cy, cx))
    area = 1
    fences = 0
    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        a, f = find_area(data, c, cy + dy, cx + dx, visited)
        area += a
        fences += f
    return area, fences


def part1(data):
    """Solve part 1"""
    fences = 0
    mx = len(data[0])
    my = len(data)
    area = []
    #peri = []
    visited = set()
    for y, row in enumerate(data):
        for x, c in enumerate(row):
            fences = 0
            # if (y - 1 < 0) or (data[y - 1][x] != c):
            #     fences += 1
            # if (x - 1 < 0) or (data[y][x - 1] != c):
            #     fences += 1
            # if (x + 1 > mx - 1) or (data[y][x + 1] != c):
            #     fences += 1
            # if (y + 1 > mx - 1) or (data[y + 1][x] != c):
            #     fences += 1
            a, f = find_area(data, c, y, x, visited)
            if a !=0:
                area.append((c, a, f))
    cost = 0
    for c, a, f in area:
        cost += a * f
    # print(area)
    return cost


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
