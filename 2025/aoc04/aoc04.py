import pathlib
import sys
from rich import print

def process(puzzle_input):
    """Parse input"""
    m = []
    for line in puzzle_input.split('\n'):
        m.append(line)
    return m

def check_condition(m, x, y):
    """Check if fewer than four rolls of paper in the neighborhood of (x, y) roll"""
    """ We will use x as row index and y as column index """
    rows = len(m)
    cols = len(m[0])
    count = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if m[nx][ny] == '@':
                    count += 1
    return True if count < 4 else False

def part1(data):
    """Solve part 1"""
    total = 0
    rows = len(data)
    cols = len(data[0])
    for i in range(rows):
        for j in range(cols):
            if data[i][j] == '@':
                if check_condition(data, i, j):
                    total += 1
    return total

def part2(data):
    """Solve part 2"""
    rows = len(data)
    cols = len(data[0])
    count = 0
    while True:
        removed = 0
        for i in range(rows):
            for j in range(cols):
                if data[i][j] == '@':
                    if check_condition(data, i, j):
                        # remove roll of paper
                        data[i] = data[i][:j] + '.' + data[i][j+1:]
                        removed += 1
                        count += 1
                        #break
        if removed == 0:
            break
    return count

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        data = process(puzzle_input)
        
        solution1 = part1(data)
        print("PART1:", solution1)
        
        solution2 = part2(data)
        print("PART2:", solution2)