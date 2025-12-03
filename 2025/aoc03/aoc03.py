import pathlib
import sys
from rich import print

def process(puzzle_input):
    """Parse input"""
    b = [] # batteries
    for line in puzzle_input.split('\n'):
        b.append(line)
    print(b)
    return b

def find_max(b):
    max_joltage = 0
    for i in range(9, 0, -1):
        x = b.find(str(i))
        if x == -1:
            continue
        for j in range(9, 0, -1):
            y = b.find(str(j), x + 1)
            if y == -1:
                continue
            joltage = i * 10 + j
            if joltage > max_joltage:
                max_joltage = joltage
    return max_joltage


def find_max12(b: str) -> int:
    """Find the maximum 12-digit integer obtainable from `b` by choosing
    12 characters in order (a subsequence). Returns 0 if impossible.

    Strategy: greedy left-to-right. For each digit position k (0..11) pick the
    largest possible digit (9..0) whose first occurrence leaves enough
    characters to complete the remaining positions.
    """
    needed = 12
    n = len(b)
    if n < needed:
        print("Not enough digits in", b, "for 12-digit number")
        return 0

    pos = 0
    digits = []
    # For each required output digit, choose the largest possible digit
    # that appears at or after `pos` and still leaves room for remaining picks.
    for remaining in range(needed, 0, -1):
        found = False
        # search digits from '9' down to '0'
        for d in range(9, -1, -1):
            ch = str(d)
            idx = b.find(ch, pos)
            if idx == -1:
                continue
            # make sure there are at least `remaining-1` chars after idx
            if n - (idx + 1) >= (remaining - 1):
                digits.append(ch)
                pos = idx + 1
                found = True
                break
        if not found:
            # no valid digit found -> impossible
            print("Unable to form 12-digit number from", b)
            return 0

    value = int(''.join(digits))
    return value

def part1(data):
    """Solve part 1"""
    return sum(find_max(b) for b in data)

def part2(data):
    """Solve part 2"""
    return sum(find_max12(b) for b in data)

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        data = process(puzzle_input)

        solution1 = part1(data)
        print("PART1:", solution1)

        solution2 = part2(data)
        print("PART2:", solution2)