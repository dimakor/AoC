import pathlib
import sys
from rich import print

def process(puzzle_input):
    """Parse input"""
    #for line in puzzle_input.split('\n'):
    return puzzle_input.split('\n')
        

def part1(data):
    """Solve part 1"""
    zero = 0 # counter for zeroes
    pointer = 50 # current position of the safe's dial
    for c in data:
        if c[0] == 'L':
            pointer -= int(c[1:])
            while pointer < 0:
                pointer += 100
        elif c[0] == 'R':
            pointer += int(c[1:])
            while pointer >= 100:
                pointer -= 100
        if pointer == 0:
            zero += 1
    return zero

def part2(data):
    """Solve part 2"""
    zero = 0 # counter for zeroes
    pointer = 50 # current position of the safe's dial
    for c in data:
        if c[0] == 'L':
            if pointer == 0:
                zero -= 1
            pointer -= int(c[1:])
            while pointer < 0:
                zero += 1
                pointer += 100
            if pointer == 0:
                zero += 1
        elif c[0] == 'R':
            pointer += int(c[1:])
            while pointer >= 100:
                zero += 1
                pointer -= 100
        print("Command:", c, "Pointer:", pointer, "Zeroes:", zero)
    return zero

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        data = process(puzzle_input)
        solution1 = part1(data)
        solution2 = part2(data)
        print("PART1:", solution1)
        print("PART2:", solution2)