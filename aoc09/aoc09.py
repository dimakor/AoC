import pathlib
import sys
from rich import print
from tqdm import tqdm

def process(puzzle_input):
    """Parse input"""
    line = list(puzzle_input)
    dense = [int(x) for x in line]
    ft = {}
    pointer = p = 0
    fileid = id = 0
    unpack = []
    es = []
    # unpack data for normal representation
    for i in range(len(dense)):
        if (i==0) or (i % 2 == 0): # file
            for j in range(dense[i]):
                unpack.append(id)
            id += 1
        else: # empty space
            for j in range(dense[i]):
                unpack.append('.')
    # fill file table
    for i in range(0, len(dense), 2):
        ft[fileid] = [pointer + length for length in range(dense[i])]
        pointer += dense[i]
        if i < len(dense) - 1:
            pointer += dense[i+1] # empty space
        fileid += 1
    return unpack, ft
        

def part1(data):
    """Solve part 1"""
    unpack, _ = data
    unpack = unpack.copy()
    file = len(unpack)
    w = 0 # write pointer
    m = file-1 # read from location pointer
    res = 0
    while w < m:
        if unpack[w] != '.':
            res += w*unpack[w]
            w += 1
            continue
        if unpack[m] == '.':
            m -= 1
            continue
        unpack[w] = unpack[m]
        unpack[m] = '.'
    return res

def part2(data):
    """Solve part 2"""
    unpack, ft = data
    file = len(unpack)
    for f in range(len(ft)-1, 1, -1):
        size = len(ft[f]) # we need SIZE empty space
        i = 0
        while i < ft[f][0]:
            if unpack[i] != '.':
                i += 1
                continue
            j = i + 1
            while j < file and unpack[j] == '.':
                j += 1
            if j-i < size:
                i = j
                continue
            for d in range(size):
                unpack[i + d] = unpack[ft[f][d]]
                unpack[ft[f][d]] = '.'
            break
    res = 0
    for i, w in enumerate(unpack):
        if w != '.':
            res += i*w
    return res



if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        data = process(puzzle_input)
        solution1 = part1(data)
        solution2 = part2(data)
        print("PART1:", solution1)
        print("PART2:", solution2)