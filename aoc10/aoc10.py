import pathlib
import sys
from rich import print


def process(puzzle_input):
    """Parse input"""
    island = []
    trailheads = []
    for y, line in enumerate(puzzle_input.split("\n")):
        l = []
        for x, c in enumerate(list(line)):
            l.append(int(c))
            if c == "0":
                trailheads.append((y, x))
        island.append(l)
    # print(island)
    # print(trailheads)
    return island, trailheads


def find_trail_score(island, start):
    # start is coordinates of single trailhead (y, x)
    maxx = len(island[0])
    maxy = len(island)
    stack = [(start, 1)]
    score = 0
    visited = set()
    tops = set()
    h = 1  # height we're looking for in the beggining
    while stack:
        p, h = stack.pop()
        if p in visited:
            continue
        for y, x in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            try:
                nx = p[1] + x
                ny = p[0] + y
                if (nx < 0) or (ny < 0):
                    continue
                if island[ny][nx] == h:
                    visited.add(p)
                    if h < 9:
                        stack.append(((ny, nx), h + 1))
                    else:
                        if (ny, nx) not in tops:
                            score += 1
                            tops.add((ny, nx))
            except:
                pass
    # for v in list(visited):
    #     island[v[0]][v[1]] = '#'
    # print_island(island)
    return score


def print_island(island):
    for line in island:
        print("".join([str(c) for c in line]))


def part1(data):
    """Solve part 1"""
    island, trailheads = data
    score = 0
    for t in trailheads:
        score += find_trail_score(island, t)
    # score = find_trail(island, (6, 0))
    return score

def find_trail_rating(island, start, h):
    p = start
    rating = 0
    if h == 9:
        return 1
    for y, x in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        try:
            nx = p[1] + x
            ny = p[0] + y
            if (nx < 0) or (ny < 0):
                continue
            if island[ny][nx] == h+1:
                rating += find_trail_rating(island, (ny, nx), h+1)
        except:
                pass
    return rating


def part2(data):
    """Solve part 2"""
    island, trailheads = data
    rating = 0
    for t in trailheads:
        rating += find_trail_rating(island, t, 0)
    return rating

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        data = process(puzzle_input)
        solution1 = part1(data)
        solution2 = part2(data)
        print("PART1:", solution1)
        print("PART2:", solution2)
