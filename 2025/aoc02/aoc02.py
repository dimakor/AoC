import pathlib
import sys
from rich import print

def process(puzzle_input):
    """Parse input"""
    d = []
    for line in puzzle_input.split(','):
        a = line.split('-')
        d.append([int(a[0]), int(a[1])])
    return d
        
def check_invalid_id(id):
    """Check if the given id is valid"""
    txt = str(id)
    l = len(txt)
    if l%2 != 0:
        return False
    txt1 = txt[:l//2]
    txt2 = txt[l//2:]
    return True if txt1 == txt2 else False

def part1(data):
    """Solve part 1"""
    inv = 0
    for a, b in data:
        # print(a, b)
        for i in range(a, b+1):
            if check_invalid_id(i):
                # print("Invalid ID found:", i)
                inv += i
    return inv

def check_invalid_id_2(id):
    """Check if the given id is valid for part 2"""
    txt = str(id)
    l = len(txt)
    # print("TXT:", txt, " L:", l, " Half:", l//2)
    for i in range(1, l//2+1):
        if l%i != 0:
            continue
        if txt[:i]*(l//i) == txt:
            return True
    return False

def part2(data):
    """Solve part 2"""
    inv = 0
    for a, b in data:
        # print("INT:", a, b)
        for i in range(a, b+1):
            if check_invalid_id_2(i):
                # print("Invalid ID found:", i)
                inv += i
    return inv

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        data = process(puzzle_input)
        solution1 = part1(data)
        solution2 = part2(data)
        print("PART1:", solution1)
        print("PART2:", solution2)