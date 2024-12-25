import pathlib
import sys
from rich import print

def get_signature(i, data):
    signature = [0] * 5
    if data[i] == '#####':
        # lock
        R = range(1, 7)
    else:
        # key
        R = range(0, 6)
    for j in R:
        for k in range(5):
            if data[i+j][k] == '#':
                signature[k] +=1
    return signature

def process(puzzle_input):
    """Parse input"""
    p = 0
    keys = []
    locks = []
    data = puzzle_input.split('\n')
    for i in range(0, len(data), 8):
        if data[i] == '#####':
            locks.append(get_signature(i, data))
        else:
            keys.append(get_signature(i, data))
    print(keys)
    print(locks)
    return keys, locks
        

def part1(data):
    """Solve part 1"""
    keys, locks = data
    res = 0
    for k in keys:
        for l in locks:
            fit = True
            for i in range(5):
                if k[i] + l[i] >5:
                    fit = False
                    break
            if fit:
                res += 1
    return res

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