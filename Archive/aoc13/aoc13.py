import pathlib
import sys
from rich import print
import parse
import json
from functools import cmp_to_key

def process(puzzle_input):
    """Parse input"""
    i = 0
    data = []
    for line in puzzle_input.split('\n'):
        if line:
            jlist = json.loads(line)
            data.append(jlist)
    return data
        
def compare_lists(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left > right:
            return 1
        else:
            return 0
    if isinstance(left, list) and isinstance(right, list):
        llen = len(left)
        rlen = len(right)
        # print(left)
        # print(right)
        for i in range(min(llen, rlen)):
            l = left[i]
            r = right[i]
            if (c:=compare_lists(l,r))!=0:
                return c
        if llen > rlen:
            return 1
        elif llen == rlen:
            return 0
        else:
            return -1
            
    if isinstance(left, int):
        return compare_lists([left], right)
    if isinstance(right, int):
        return compare_lists(left, [right])

def part1(data):
    """Solve part 1"""
    index = 1
    total = 0
    for i in range(0, len(data), 2):
        cmp = compare_lists(data[i], data[i+1])
        if cmp!=1:
            total += index
        index +=1
    return total

def part2(data):
    """Solve part 2"""
    data.append([[2]])
    data.append([[6]])
    #print(data)
    sdata = sorted(data, key=cmp_to_key(compare_lists))
    key = 1
    for i, l in enumerate(sdata):
        if l == [[2]] or l == [[6]]:
            key *= i+1
    return key

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text()
        data = process(puzzle_input)
        solution1 = part1(data)
        solution2 = part2(data)
        print("PART1:", solution1)
        print("PART2:", solution2)