import pathlib
import sys
from rich import print


def process(puzzle_input):
    """Parse input"""
    eos = False  # end of section
    fresh = []  # set of fresh ingridients
    ids = []
    for n, line in enumerate(puzzle_input.split("\n")):
        if not eos:
            # ranges of fresh ingridients
            if not line:
                # end of ranges section reached
                eos = True
                continue
            parts = line.split("-")
            low = int(parts[0])  # lower bound
            high = int(parts[1])  # upper bound
            fresh.append(range(low, high + 1))
        else:
            # IDs of ingridients
            if line:
                ids.append(int(line))
    return fresh, ids


def part1(data):
    """Solve part 1"""
    fresh, ids = data
    count = 0
    for i in ids:
        for r in fresh:
            if i in r:
                count += 1
                break
    return count

def ranges_intersect(r1, r2):
    return r1.start < r2.stop and r2.start < r1.stop

def range_union(r1, r2):
    start = min(r1.start, r2.start)
    stop = max(r1.stop, r2.stop)
    if start < stop:
        return range(start, stop)
    return None  # no intersection

def part2(data):
    """Solve part 2 - calculate total unique numbers in all ranges"""
    fresh, _ = data
    fresh = sorted(fresh, key=lambda r: r.start)
    
    # Merge overlapping ranges
    merged = []
    for r in fresh:
        if not merged:
            merged.append(r)
        else:
            last = merged[-1]
            # Check if current range overlaps with last merged range
            if r.start <= last.stop:
                # Merge: extend the stop to cover both ranges
                merged[-1] = range(last.start, max(last.stop, r.stop))
            else:
                # No overlap, add as new range
                merged.append(r)
    
    # Sum lengths of all merged ranges
    total = sum(len(r) for r in merged)
    return total

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        data = process(puzzle_input)

        solution1 = part1(data)
        print("PART1:", solution1)

        solution2 = part2(data)
        print("PART2:", solution2)
