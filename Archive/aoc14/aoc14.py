import pathlib
import sys
from rich import print
from parse import parse
import re
SAND = [500,0]

def draw_line(cave, p1, p2):
    if p1[0] == p2[0]:
        # vertical line
        l = int(p1[1]) - int(p2[1])
        p = int(p2[1]) if l > 0 else int(p1[1])
        for i in range(abs(l)+1):
            cave[p+i][int(p1[0])] = '#'
    else:
        # horizontal line
        l = int(p1[0]) - int(p2[0])
        p = int(p2[0]) if l > 0 else int(p1[0])
        for i in range(abs(l)+1):
            cave[int(p1[1])][p+i] = '#'

def process_line(cave, points):
    for i in range(len(points)-1):
        draw_line(cave, points[i], points[i+1])

def print_cave(cave):
    for line in cave:
        print(''.join(line)[490:550])

def sand_fall(cave):
    s = list(SAND)
    while True:
        if cave[s[1]+1][s[0]] == '.':
            s[1] += 1
            continue
        elif (cave[s[1]+1][s[0]] == '#') or (cave[s[1]+1][s[0]] == 'o'):
            if cave[s[1]+1][s[0]-1] == '.':
                s[1] += 1
                s[0] -= 1
                continue
            elif cave[s[1]+1][s[0]+1] == '.':
                s[1] += 1
                s[0] += 1
                continue
        cave[s[1]][s[0]] = 'o'
        break
    return s


def process(puzzle_input):
    """Parse input"""
    points = puzzle_input.split()
    max  = 0
    for i in points:
        c = i.find(',')
        if c != -1:
            y = int(i[c+1:])
            max = y if y > max else max
    
    max += 5
    cave = [list("."*520) for i in range(max)]
    #print(cave)
    p = re.compile(r'(\d*),(\d*)')
    for line in puzzle_input.split('\n'):
        process_line(cave, p.findall(line))
    i = 0
    try:
        while True:
            sand_fall(cave)
            i += 1
    except IndexError:
        pass
    return i
        

def part1(data):
    """Solve part 1"""
    return data

def part2(data):
    """Solve part 2"""
    """Parse input"""
    points = puzzle_input.split()
    max  = 0
    for i in points:
        c = i.find(',')
        if c != -1:
            y = int(i[c+1:])
            max = y if y > max else max
    
    max += 2
    cave = [list("."*1000) for i in range(max)]
    cave.append(list("#"*1000))
    #print(cave)
    p = re.compile(r'(\d*),(\d*)')
    for line in puzzle_input.split('\n'):
        process_line(cave, p.findall(line))
    i = 0
    s = [1,1]
    try:
        while (s[0] != SAND[0]) or (s[1] != SAND[1]):
            s = sand_fall(cave)
            i += 1
    except IndexError:
        pass
    print_cave(cave)
    print(s)
    return i

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text()
        data = process(puzzle_input)
        solution1 = part1(data)
        solution2 = part2(puzzle_input)
        print("PART1:", solution1)
        print("PART2:", solution2)