import pathlib
import sys
from rich import print

global total
total = 0

def get_wd(disk, p):
    wd = disk
    for i in p:
        wd = wd[i]
    return wd

def get_dir_size(dirsize: dict, disk:dict):
    global total
    ds = 0
    for key, value in disk.items():
        if isinstance(value, dict):
            x = get_dir_size(dirsize, value)
            if x<=100000:
                total += x
            dirsize[key] = x
            ds += x
        else:
            ds += value
    return ds
     
def parse(puzzle_input):
    """Parse input"""
    global total
    disk = {}
    p = []
    cwd = disk
    for line in puzzle_input.split('\n'):
        if line == "$ cd /":
            p = []
            continue
        elif line == "$ cd ..":
            p.pop()
            cwd = get_wd(disk, p)
            continue
        elif "$ cd" in line:
            p.append(line[5:])
            cwd = cwd[line[5:]]
            continue
        elif "$ ls" in line:
            continue
        elif "dir" in line[0:3]:
            cwd[line[4:]] = {}
            continue
        else:
            file = line.split()
            cwd[file[1]] = int(file[0])
    dirsize={}
    dirsize['/'] = get_dir_size(dirsize, disk)
    print(dirsize)
    print("TOTAL:", total)
    return dirsize

def part1(data):
    """Solve part 1"""
    for i in range(3, len(data)+1):
        buf = set([data[j] for j in range(i-3, i+1)])
        #print("I:",i, "BUF:", buf)
        if len(buf) == 4:
            return i+1

def part2(data):
    """Solve part 2"""
    for i in range(13, len(data)+1):
        buf = set([data[j] for j in range(i-13, i+1)])
        #print("I:",i, "BUF:", buf)
        if len(buf) == 14:
            return i+1

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    dirsize = parse(puzzle_input)
    files = dirsize['/']
    print("/:", files)
    free = 70000000-files
    print("UNUSED:", free)
    need = 30000000 - free
    print("NEED:", need)
    a = sorted(dirsize.items(), key=lambda x: x[1])    
    for key, value in a:
        if value >= need:
            print(key, value)
            break


    #return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        #print("\n".join(str(solution) for solution in solutions))