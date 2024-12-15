import pathlib
import sys
from rich import print


def process(puzzle_input):
    """Parse input"""
    warehouse = []
    program = []
    ismap = True
    lines = []
    robot = None
    for line in puzzle_input.split("\n"):
        if line == "":
            ismap = False
        if ismap:
            warehouse.append(list(line))
            try:
                x = line.index("@")
                robot = (len(warehouse) - 1, x)
            except ValueError:
                pass
        else:
            lines.append(line)
    program = list(''.join(lines))
    printwh(warehouse)
    print(program)
    return warehouse, program, robot


CMD = {
    ">": (0, 1),
    "<": (0, -1),
    "^": (-1, 0),
    "v": (1, 0),
}

def move(warehouse, place, command):
    m = (place[0] + command[0], place[1] + command[1])
    w = warehouse[m[0]][m[1]] 
    if w == '.':
        warehouse[m[0]][m[1]] = warehouse[place[0]][place[1]]
        warehouse[place[0]][place[1]] = '.'
        return True
    elif w == 'O':
        if move(warehouse, m, command):
            warehouse[m[0]][m[1]] = warehouse[place[0]][place[1]]
            warehouse[place[0]][place[1]] = '.'
            return True
    elif w == '#':
        return False

def GPS(warehouse):
    coord = 0
    for y, line in enumerate(warehouse):
        for x, c in enumerate(line):
            if c == 'O':
                coord += 100*y + x
    return coord

def part1(data):
    """Solve part 1"""
    warehouse, program, robot = data
    for c in program:
        if move(warehouse, robot, CMD[c]):
            robot = (robot[0] + CMD[c][0], robot[1] + CMD[c][1])
    printwh(warehouse)
    return GPS(warehouse)


def part2(data):
    """Solve part 2"""

def printwh(warehouse):
    for line in warehouse:
        print(''.join(line))

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        data = process(puzzle_input)
        solution1 = part1(data)
        solution2 = part2(data)
        print("PART1:", solution1)
        print("PART2:", solution2)
