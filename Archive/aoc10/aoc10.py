# aoc06.py

import pathlib
import sys
from rich import print

SIG = [39, 79, 119, 159, 199, 239]

def parse(puzzle_input):
    """Parse input"""

def part1(puzzle_input):
    """Solve part 1"""
    tick = 0
    X = 1
    STR = 0
    for line in puzzle_input.split('\n'):
        print(line)
        if line == "noop":
            tick +=1
            if tick in SIG:
                STR += (tick+1) * X
            print("TICK:", tick, "  X:", X)
        elif "addx" in line:
            tick +=1       
            print("TICK:", tick, "  X:", X)
            if tick in SIG:
                STR += (tick+1) * X
            tick +=1       
            X += int(line[5:]) 
            print("TICK:", tick, "  X:", X)
            if tick in SIG:
                STR += (tick+1) * X
    print(STR)

def part2(puzzle_input):
    """Solve part 2"""
    tick = 0
    X = 1
    draw = '' 
    for line in puzzle_input.split('\n'):
        if line == "noop":
            tick +=1
            if tick in [X-1, X, X+1]:
                draw +='#'
            else:
                draw +='.'
            if tick == 40:
                print(draw)
                draw = ''
                tick = 0
        elif "addx" in line:
            tick +=1       
            if tick in [X-1, X, X+1]:
                draw +='#'
            else:
                draw +='.'
            if tick == 40:
                print(draw)
                draw = ''
                tick = 0
            tick +=1     
            X += int(line[5:]) 
            if tick in [X-1, X, X+1]:
                draw +='#'
            else:
                draw +='.'  
            if tick == 40:
                print(draw)
                draw = ''
                tick = 0
    #print(draw)

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    #data = parse(puzzle_input)
    #solution1 = part1(puzzle_input)
    solution2 = part2(puzzle_input)

    return solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        #print("\n".join(str(solution) for solution in solutions))