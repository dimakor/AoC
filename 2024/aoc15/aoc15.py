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
    return GPS(warehouse)

def check4(warehouse, a1, a2, move):
    # move == +1 or -1 to move up or down
    neighbour = 0
    m1 = (a1[0] + move, a1[1])
    m2 = (a2[0] + move, a2[1])
    if warehouse[m1[0]][m1[1]] == '#' or warehouse[m2[0]][m2[1]] == '#':
        return False
    if warehouse[m1[0]][m1[1]] == '.' and warehouse[m2[0]][m2[1]] == '.':
        return True
    if warehouse[m1[0]][m1[1]] == warehouse[a1[0]][a1[1]]:
        return check4(warehouse, m1, m2, move)
    if a1[0] < a2[0]:
        check1 = check4(warehouse, (m1[0]-1, m1[1]), m1, move)
        check2 = check4(warehouse, m2, (m2[0]+1, m2[1]), move)
        if check1 and check2:
            return True
        else:
            return False
    else:
        check1 = check4(warehouse, m1, (m1[0]+1, m1[1]), move)
        check2 = check4(warehouse,  (m2[0]-1, m2[1]), m2, move)
        if check1 and check2:
            return True
        else:
            return False
        

def move2(warehouse, place, command, second = None):
    if command[1] == 0:
        # vertical movement
        m = (place[0] + command[0], place[1] + command[1])
        w = warehouse[m[0]][m[1]] 
        if second: # should be coordinate of second part of box
            m2 = (second[0] + command[0], second[1] + command[1])
            w2 = warehouse[m2[0]][m2[1]]
            if w == '.' and w2 == '.':
                warehouse[m[0]][m[1]] = warehouse[place[0]][place[1]]
                warehouse[m2[0]][m2[1]] = warehouse[second[0]][second[1]]
                return True
            elif w == '#' or w2 == '#':
                return False
            else:
                if w == warehouse[place[0]][place[1]]: # the box exactly over/under our box
                    if move2(warehouse, m, command, m2):
                        warehouse[m[0]][m[1]] = warehouse[place[0]][place[1]]
                        warehouse[m2[0]][m2[1]] = warehouse[second[0]][second[1]]
                        warehouse[place[0]][place[1]] = '.'
                        warehouse[second[0]][second[1]] = '.'
                        return True
                else: # 4 boxes at once
                    if check4(warehouse, m, m2, command[1]):
                        move2(warehouse, m, command, m2)
                        warehouse[m[0]][m[1]] = warehouse[place[0]][place[1]]
                        warehouse[m2[0]][m2[1]] = warehouse[second[0]][second[1]]
                        warehouse[place[0]][place[1]] = '.'
                        warehouse[second[0]][second[1]] = '.'
                    else:
                        return False
        else:
            if w == '#':
                return False
            elif w == '.':
                warehouse[m[0]][m[1]] = warehouse[place[0]][place[1]]
                warehouse[place[0]][place[1]] = '.'
                return True
            elif w == '[':
                second = (m[0], m[1]+1)
            elif w == ']':
                second = (m[0], m[1]-1)
            if move2(warehouse, m, command, second):
                warehouse[m[0]][m[1]] = warehouse[place[0]][place[1]]
                warehouse[place[0]][place[1]] = '.'
                return True
    else:
        m = (place[0] + command[0], place[1] + command[1])
        w = warehouse[m[0]][m[1]] 
        if w == '.':
            warehouse[m[0]][m[1]] = warehouse[place[0]][place[1]]
            warehouse[place[0]][place[1]] = '.'
            return True
        elif w in ['[', ']']:
            if move2(warehouse, m, command):
                warehouse[m[0]][m[1]] = warehouse[place[0]][place[1]]
                warehouse[place[0]][place[1]] = '.'
                return True
        elif w == '#':
            return False
    
def part2(data):
    """Solve part 2"""

def printwh(warehouse):
    for line in warehouse:
        print(''.join(line))

def process2(warehouse):
    """Parse input"""
    warehouse2 = []
    robot = None
    for line in warehouse:
        line2 = []
        for c in line:
            if c == '@':
                line2.append('@')
                line2.append('.')
                robot = (len(warehouse2), len(line2) - 2)
            elif c == 'O':
                line2.append('[')
                line2.append(']')
            else:
                line2.append(c)
                line2.append(c)
        warehouse2.append(line2)
    printwh(warehouse2)
    print(robot)
    return warehouse2, robot

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        data = process(puzzle_input)
        warehouse2, robot = process2(data[0].copy())
        #solution1 = part1(data)
        solution2 = part2((warehouse2, robot, data[2]))
        printwh(warehouse2)
        #print("PART1:", solution1)
        print("PART2:", solution2)
