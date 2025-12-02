import pathlib
import sys
from rich import print
from tqdm import tqdm
from functools import cache

def process(puzzle_input):
    """Parse input"""
    return [int(num) for num in puzzle_input.split(' ')]

        

def part1(data):
    """Solve part 1"""
    print(data)
    stones = data
    nstones = []
    for blink in tqdm(range(75)): # number of blinks
        n = len(stones)
        for i in range(n):
            st = stones[i]
            if st == 0:
                nstones.append(1)
            elif (x:=len(s:=str(st))) % 2 == 0:
                m = 10**(x/2)
                st1 = int(st/m)
                st2 = st - int(st1*m)
                nstones.append(st1)
                nstones.append(st2)
            else:
                nstones.append(st * 2024)
        stones = nstones
        nstones = []
    #print(stones)
    return(len(stones))
            
@cache
def total_stones(value, turns_remaining):
    while turns_remaining > 0:
        if value == 0:
            value = 1
            turns_remaining -= 1
        elif len(str(value)) % 2 == 0:
            first_half = str(value)[:len(str(value)) // 2]
            second_half = str(value)[len(str(value)) // 2:]
            turns_remaining -= 1
            total = 0
            total += total_stones(int(first_half), turns_remaining)
            total += total_stones(int(second_half), turns_remaining)
            return total
        else:
            value = value * 2024
            turns_remaining -= 1
    return 1

def part2(data):
    """Solve part 2"""
    turns = 75
    total = 0
    for n in data:
        total += total_stones(n, turns)
    return total

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        data = process(puzzle_input)
        #solution1 = part1(data)
        solution2 = part2(data)
        #print("PART1:", solution1)
        print("PART2:", solution2)