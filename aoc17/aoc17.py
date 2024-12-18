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
        A = 117440
        B = 0
        C = 0
        PRG = "0,3,5,4,3,0".split(',')
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

def part1(data, onetime=False):
    """Solve part 1"""
    A, B, C, PRG = data
    p = 0
    res = ''
    while p < len(PRG):
        opcode = int(PRG[p])
        operand = int(PRG[p+1])

        # adv
        if opcode == 0:
            A = A // 2 ** combo(operand, A, B, C)
        # bxl
        elif opcode == 1:
            B = B ^ operand
        # bst
        elif opcode == 2:
            B = int(combo(operand, A, B, C) % 8)
        # jnz
        elif opcode == 3:
            if A == 0 or onetime:
                if onetime:
                    return res
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
    return res[:-1]

def part2(data):
    """Solve part 2"""
    _, B, C, PRG = data
    values = PRG.copy()#[PRG[x] for x in range(1, len(PRG), 2)]
    results = []
    find_solutions(values, PRG, 0, results, 1)
    if len(results):
        print("pt 2: smallest reg_a:", sorted(results)[0])
    x = part1((results[0], 0,0, PRG))
    print("X", x)    
    return results[0]

def find_solutions(values, program, a, results, level):
    val = values[-level]
    for i in range(0, 8):
        test = part1((a+i, 0, 0, program), True)
        if test[0] == val:
            if level == len(values):
                results.append(a+i)
                print("valid a:", a+i)
            elif level < len(values):
                find_solutions(values, program, (a+i) * 8, results, level+1)

if __name__ == "__main__":
    # for path in sys.argv[1:]:
        # print(f"{path}:")
        # puzzle_input = pathlib.Path(path).read_text().strip()
    data = process(True)
    solution1 = part1(data)
    solution2 = part2(data)
    print("PART1:", solution1)
    print("PART2:", solution2)