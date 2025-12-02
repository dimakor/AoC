import pathlib
import sys
from rich import print

dcache = dict()

def process(puzzle_input):
    """Parse input"""
    inp = True
    ava = []
    des = []
    for line in puzzle_input.split('\n'):
        if inp:
            ava = line.split(', ')
            inp = False
        else:
            if not line:
                continue
            des.append(line)
    print(ava)
    print(des)
    return ava, des

def splitword(design, ava):
    if not design:
        return 1
    if design in dcache:
        return dcache[design]
    matches = 0
    for word in ava:
        if design.startswith(word):
            new_design = design[len(word):]
            s = splitword(new_design, ava)
            matches += s
    dcache[design] = matches
    return matches

def part1(data):
    """Solve part 1"""
    ava, des = data
    count = 0
    matches = 0
    for pattern in des:
        print("PATTERN:", pattern)
        if s := splitword(pattern, ava):
            count += 1
            matches +=s
        else:
            print("IMP:", pattern)
    return count, matches


def part2(data):
    """Solve part 2"""

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        data = process(puzzle_input)
        solution1, solution2 = part1(data)
        #solution2 = part2(data)
        print("PART1:", solution1)
        print("PART2:", solution2)