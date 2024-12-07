import pathlib
import sys
from rich import print

def process(puzzle_input):
    """Parse input"""
    sum = []
    num = []
    for line in puzzle_input.split('\n'):
        sum.append(int(line[:line.index(':')]))
        nsum = []
        for n in line[line.index(':')+2:].split(' '):
            nsum.append(int(n))
        num.append(nsum)
    return sum, num

        

def part1(data):
    """Solve part 1"""
    sum, num = data
    total = 0
    s2 = []
    n2 = []
    for s, n in zip(sum, num):
        miss = True
        for i in range(2**(len(n)-1)):
            res = n[0]
            for j in range(len(n)-1):
                if i & 2**j == 2**j:
                    res += n[j+1]
                else:
                    res *= n[j+1]
                if res > s:
                    break
            if res == s:
                total += s
                miss = False
                break
        if miss:
            s2.append(s)
            n2.append(n)
    return total, s2, n2



def part2(sum, num):
    """Solve part 2"""
    total = 0
    for s, n in zip(sum, num):
        for i in range(3**(len(n)-1)):
            res = n[0]
            for j in range(len(n)-1):
                mm = i % 3
                i //= 3
                if mm == 0:
                    res += n[j+1]
                elif mm == 1:
                    res *= n[j+1]
                else: 
                    res = int(str(res) + str(n[j+1]))
                if res > s:
                    break
            if res == s:
                total += s
                break
    return total

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        data = process(puzzle_input)
        solution1, s2, n2 = part1(data)
        solution2 = part2(s2, n2)
        print("PART1:", solution1)
        print("PART2:", solution1+solution2)