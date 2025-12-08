import pathlib
import sys
from rich import print

def process(puzzle_input):
    """Parse input"""
    sheet = []
    for line in puzzle_input.split('\n'):
        sl = line.split()
        sheet.append(sl)
    return sheet
            

def part1(data):
    """Solve part 1"""
    gtotal = 0
    for i in range(len(data[0])):
        if data[-1][i] == '+':
            gtotal += sum(int(row[i]) for row in data[:-1])
        elif data[-1][i] == '*':
            p = 1
            for row in data[:-1]:
                p *= int(row[i])
            gtotal += p
    return gtotal

def part2(puzzle_input):
    """Solve part 2"""
    sheet = []
    result = 0
    for line in puzzle_input.split('\n'):
        sheet.append(line)
    last_row = sheet[-1]+'  ' # padding for trailing spaces removed by split
    ll = len(last_row)
    for i in range(ll):
        if last_row[i] not in '+*':
                continue
        for j in range(i+1, ll):
            if (last_row[j] not in '+*') and (j < ll-1):
                continue
            if j == ll-1:
                j += 1
            result += calc(sheet, i, j-1)
            break
        i = j
    return result

def calc(sheet, i, j):
    result = 0
    for x in range(j, i-1, -1):
        nrow = len(sheet)-1
        num = 0
        for n in range(nrow):
            try:
                val = int(sheet[n][x])
            except ValueError:
                continue
            num = num*10 + val
        if sheet[-1][i] == '+':
            result += num
        elif sheet[-1][i] == '*':
            if result == 0:
                result = 1
            result *= num
    return result

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        data = process(puzzle_input)

        # solution1 = part1(data)
        # print("PART1:", solution1)

        solution2 = part2(puzzle_input)
        print("PART2:", solution2)