import pathlib
import sys
from rich import print
from tqdm import tqdm

import asyncio

def background(f):
    def wrapped(*args, **kwargs):
        return asyncio.get_event_loop().run_in_executor(None, f, *args, **kwargs)

    return wrapped

def process(puzzle_input):
    """Parse input"""
    obstacles = set()
    guardx = guardy = 0
    for i, line in enumerate(puzzle_input.split('\n')):
        for j, c in enumerate(line):
            if c == "#":
                obstacles.add((j, i))
            if c == "^":
                guardx = j
                guardy = i
    return obstacles, guardx, guardy, j+1, i+1


def part1(data):
    """Solve part 1"""
    dirx = 0
    diry = -1
    obstacles, guardx, guardy, x, y = data
    positions = set()
    positions.add((guardx, guardy))
    while True:
        if (guardx + dirx, guardy + diry) in obstacles:
            dirx, diry = -diry, dirx
            continue
        guardx += dirx
        guardy += diry
        if (guardx < 0) or (guardy < 0) or (guardx > x) or (guardy > y):
            break
        positions.add((guardx, guardy))
    return len(positions)

@background        
def check_cycle(data):
    dirx = 0
    diry = -1
    obstacles, gx, gy, x, y = data
    guardx = gx
    guardy = gy
    trail = []
    trail.append((guardx, guardy, dirx, diry))
    while True:
        if (guardx + dirx, guardy + diry) in obstacles:
            dirx, diry = -diry, dirx
            continue
        guardx += dirx
        guardy += diry
        if (guardx < 0) or (guardy < 0) or (guardx > x) or (guardy > y):
            return False
        if (guardx, guardy, dirx, diry) in trail:
            return True
        trail.append((guardx, guardy, dirx, diry))
        


def part2(data):
    """Solve part 2"""
    obstacles, guardx, guardy, x, y = data
    res = 0
    for i in tqdm(range(x)):
    # for i in range(x):
        for j in range(y):
            if ((i,j) in obstacles) or (i == guardx and j == guardy):
                continue
            obstacles.add((i,j))
            if check_cycle((obstacles, guardx, guardy, x, y)):
                res += 1
            obstacles.remove((i,j))
    return res



if __name__ == "__main__":
   for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        # puzzle_input = pathlib.Path(r"C:\Users\koroc\Documents\AoC\aoc06\test.txt").read_text().strip()
        data = process(puzzle_input)
        #solution1 = part1(data)
        solution2 = part2(data)
        #print("PART1:", solution1)
        print("PART2:", solution2)