# aoc202201.py

import pathlib
import sys
from rich import print

def parse(puzzle_input):
    """Parse input"""
    return [ [line[0], line[2]] for line in puzzle_input.split('\n')]
   
def calc_score(round):
    if round[0] == "A":
        #elf - ROCK
        if round[1] == "X":
            # you - ROCK
            return 1 + 3 #draw
        elif round[1] == "Y":
            # you - PAPER
            return 2 + 6 #win
        elif round[1] == "Z":
            # you - SCISSORS
            return 3 + 0 #lost
    elif round[0] == "B":
        #elf - PAPER
        if round[1] == "X":
            # you - ROCK
            return 1 + 0 #lost
        elif round[1] == "Y":
            # you - PAPER
            return 2 + 3 #draw
        elif round[1] == "Z":
            # you - SCISSORS
            return 3 + 6 #win
    elif round[0] == "C":
        #elf - SCISSORS
        if round[1] == "X":
            # you - ROCK
            return 1 + 6 #win
        elif round[1] == "Y":
            # you - PAPER
            return 2 + 0 #lost
        elif round[1] == "Z":
            # you - SCISSORS
            return 3 + 3 #draw

def calc_score2(round):
    if round[0] == "A":
        #elf - ROCK
        if round[1] == "X":
            # you - LOSE
            return 3 + 0 #sci
        elif round[1] == "Y":
            # you - DRAW
            return 1 + 3 #rock
        elif round[1] == "Z":
            # you - WIN
            return 2 + 6 #lost
    elif round[0] == "B":
        #elf - PAPER
        if round[1] == "X":
            # you - LOSE
            return 1 + 0 #sci
        elif round[1] == "Y":
            # you - DRAW
            return 2 + 3 #rock
        elif round[1] == "Z":
            # you - WIN
            return 3 + 6 #lost
    elif round[0] == "C":
        #elf - SCISSORS
        if round[1] == "X":
            # you - LOSE
            return 2 + 0 #sci
        elif round[1] == "Y":
            # you - DRAW
            return 3 + 3 #rock
        elif round[1] == "Z":
            # you - WIN
            return 1 + 6 #lost

def part1(data):
    """Solve part 1"""
    sum = 0
    for i in data:
        sum += calc_score(i)
    return sum

def part2(data):
    """Solve part 2"""
    sum = 0
    for i in data:
        sum += calc_score2(i)
    return sum

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))