import pathlib
import sys
from rich import print

def process(puzzle_input):
    """Parse input"""
    ant = {}
    field = []
    for i, line in enumerate(puzzle_input.split('\n')):
        field.append(list(line))
        for j, c in enumerate(line):
            if c != ".":
                try:
                    ant[c].append((j, i))
                except KeyError:
                    ant[c] = []
                    ant[c].append((j, i))
    return ant, j+1, i+1, field
        
def num_antinodes(a, b, mx, my, field):
    x1, y1 = a
    x2, y2 = b
    count = 0

    for t in [-1, 2]:
        x = x1 + t * (x2 - x1)
        y = y1 + t * (y2 - y1)
        if (0 <= x < mx) and (0 <= y < my):# and (x, y) not in allant:
            count += 1
            field[y][x] = '#'
    return count
                



def part1(data):
    """Solve part 1"""
    ant, x, y, field = data
    count = 0
    for sig, coord in ant.items():
        for p1 in coord:
            for p2 in coord:
                if p1 != p2:
                    count += num_antinodes2(p1, p2, x, y, field)
    d = 0
    for f in field:
        for i in f:
            if i == '#':
                d += 1
        print(''.join(f))
    print(d)
    return d


def num_antinodes2(a, b, mx, my, field):
    x1, y1 = a
    x2, y2 = b
    count = 0

    for t in range(mx):#range(1,mx):
        x = x1 - t * (x2 - x1)
        y = y1 - t * (y2 - y1)
        if (0 <= x < mx) and (0 <= y < my):# and (x, y) not in allant:
            count += 1
            field[y][x] = '#'
        else:
            break

    # for t in range(2, mx):
    for t in range(mx):
        x = x1 + t * (x2 - x1)
        y = y1 + t * (y2 - y1)
        if (0 <= x < mx) and (0 <= y < my):# and (x, y) not in allant:
            count += 1
            field[y][x] = '#'
        else:
            break
    return count

def part2(data):
    """Solve part 2"""
    ant, x, y, field = data
    count = 0
    acount = 0
    print("MX,MY:", x, y)
    for sig, coord in ant.items():
        for p1 in coord:
            for p2 in coord:
                if p1 != p2:
                    count += num_antinodes(p1, p2, x, y, field)
        if len(coord) > 1:
            acount += len(coord)
    d = 0
    for f in field:
        for i in f:
            if i == '#':
                d += 1
        print(''.join(f))
    print(d)
    return d# + acount

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        data = process(puzzle_input)
        solution1 = part1(data)
        solution2 = part2(data)
        print("PART1:", solution1)
        print("PART2:", solution2)