import pathlib
import sys
from rich import print
import math

def process(puzzle_input=False):
    """Parse input"""
    if puzzle_input:
        A = 33940147
        B = 0
        C = 0
        PRG = "2,4,1,5,7,5,1,6,4,2,5,5,0,3,3,0".split(',')
    else:
        A = 729
        B = 0
        C = 0
        PRG = "0,1,5,4,3,0".split(',')
    print(PRG)
    return A, B, C, PRG
        
def combo(operand, A, B, C):
    if operand in [0, 1, 2, 3]:
        return operand
    elif operand == 4:
        return A
    elif operand == 5:
        return B
    # elif operand == 6:
    return C

def part1(data):
    """Solve part 1"""
    A, B, C , PRG = data
    p = 0
    res = ''
    while p < len(PRG):
        print("P:", p)
        opcode = int(PRG[p])
        operand = int(PRG[p+1])

        # adv
        if opcode == 0:
            numerator = A
            denominator = 2 ** combo(operand, A, B, C)
            A = math.trunc(numerator/ denominator)
        # bxl
        elif opcode == 1:
            B = B ^ operand
        # bst
        elif opcode == 2:
            B = int(combo(operand, A, B, C) % 8)
        # jnz
        elif opcode == 3:
            if A == 0:
                p += 2
                continue
            p = combo(operand, A, B, C)
            continue
        # bxc
        elif opcode == 4:
            B = B ^ C
        # out
        elif opcode == 5:
            # print(combo(operand, A, B, C) % 8, ",")
            res += str(combo(operand, A, B, C) % 8) + ","
        # bdv
        elif opcode == 6:
            numerator = A
            denominator = 2 ** combo(operand, A, B, C)
            B = math.trunc(numerator/ denominator)
        # cdv
        elif opcode == 7:
            numerator = A
            denominator = 2 ** combo(operand, A, B, C)
            C = math.trunc(numerator/ denominator)
        p +=2
    return res

def part2(data):
    """Solve part 2"""

if __name__ == "__main__":
    # for path in sys.argv[1:]:
        # print(f"{path}:")
        # puzzle_input = pathlib.Path(path).read_text().strip()
    data = process(True)
    solution1 = part1(data)
    solution2 = part2(data)
    print("PART1:", solution1)
    print("PART2:", solution2)