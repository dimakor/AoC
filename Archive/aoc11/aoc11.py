import pathlib
import sys
from rich import print
import time
from rich.progress import track

def process(puzzle_input):
    """Parse input"""
    lines = puzzle_input.split('\n')
    M = (len(lines)+1) // 7 # number of monkeys and blocks in input
    items = [] 
    op = []
    num = []
    cond = []
    act={}
    for i in range(M):
        items.append([int(j) for j in lines[i*7+1][18:].split(', ')])
        o = lines[i*7+2][23]
        if o == '+':
            op.append('+')
            num.append(int(lines[i*7+2][25:]))
        elif o == '*':
            if 'old' in lines[i*7+2][25:]:
                op.append('^')
                num.append(lines[i*7+2][25:])
            else:
                op.append('*')
                num.append(int(lines[i*7+2][25:]))
        cond.append(int(lines[i*7+3][21:]))
        act[i]={True : int(lines[i*7+4][29:]), False : int(lines[i*7+5][29:])}
    return M, items, op, num, cond, act

def calc(level, operation, amount):
    if operation == '^':
        return level*level
    elif operation == '*':
        return level * amount
    return level + amount

def part1(M, items, op, num, cond, act):
    """Solve part 1"""
    mb = [0 for _ in range(M)]
    for round in range(20):
        for m in range(M):
            mb[m] += len(items[m])
            for i in range(len(items[m])):
                item = items[m].pop(0)
                wr = calc(item, op[m], num[m])
                nwr = wr//3
                items[act[m][nwr % cond[m] == 0]].append(nwr)
    mb.sort(reverse=True)
    print(mb)
    return mb[0]*mb[1]



def part2(M, items, op, num, cond, act):
    """Solve part 2"""
    mb = [0 for _ in range(M)]
    divby = 1
    for c in cond:
        divby *= c
    for round in track(range(10000), description="Processing..."):
        for m in range(M):
            mb[m] += len(items[m])
            for i in range(len(items[m])):
                item = items[m].pop(0)
                wr = calc(item, op[m], num[m])
                nwr = wr % divby
                items[act[m][nwr % cond[m] == 0]].append(nwr)
    print("MB:", mb)
    mb.sort(reverse=True)
    return mb[0]*mb[1]

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        M, items, op, num, cond, act = process(puzzle_input)

        #solution1 = part1(M, items, op, num, cond, act)
        solution2 = part2(M, items, op, num, cond, act)
        #print("PART1:", solution1)
        print("PART2:", solution2)