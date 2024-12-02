# aoc05.py

import pathlib
import sys
from rich import print
import parse as prs

def parse(puzzle_input):
    """Parse input"""
    lines = puzzle_input.split('\n')
    for i, line in enumerate(lines):
        if not line:
            break
    # step 1: load stacks
    stacks = int((len(lines[i-1])+1)/4) # number of stacks
    field = [[] for _ in range(0, stacks)]
    for level in range(i-2, -1, -1):
        print(lines[level])
        for c in range(0, stacks):
            if lines[level][c*4+1] == ' ':
                continue
            field[c].append(lines[level][c*4+1])
    # step 2: load instructions
    program = lines[i+1:]
    return field, program

def part1(field, program):
    """Solve part 1"""
    print(field)
    PATTERN = prs.compile("move {num:d} from {from:d} to {to:d}")
    for step in program:
        prg = PATTERN.search(step)
        for _ in range(0, prg.named['num']):
            crate = field[prg.named['from']-1].pop()
            field[prg.named['to']-1].append(crate)
    print(field)
    answer = []
    for crate in field:
        answer.append(crate[-1])
    print(''.join(answer))



def part2(field, program):
    """Solve part 2"""
    print(field)
    PATTERN = prs.compile("move {num:d} from {from:d} to {to:d}")
    for step in program:
        prg = PATTERN.search(step)
        nb = prg.named['num']
        for bb in range(0, nb):
            crate = field[prg.named['from']-1].pop(bb-nb)
            field[prg.named['to']-1].append(crate)
    print(field)
    answer = []
    for crate in field:
        answer.append(crate[-1])
    print(''.join(answer))

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    field, program = parse(puzzle_input)
    #solution1 = part1(field, program)
    solution2 = part2(field, program)

    return solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text()
        solutions = solve(puzzle_input)
        #print("\n".join(str(solution) for solution in solutions))