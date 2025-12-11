import pathlib
import sys
from rich import print

from itertools import combinations
from tqdm import tqdm
import math

def distance_3d(p1, p2):
    """Distance between two 3D points (tuples or lists: (x, y, z))"""
    return math.sqrt(sum((a - b)**2 for a, b in zip(p1, p2)))

def distance_3d_nosqrt(p1, p2):
    """Distance between two 3D points (tuples or lists: (x, y, z))"""
    return sum((a - b)**2 for a, b in zip(p1, p2))

def process(puzzle_input):
    """Parse input"""
    boxes = []
    distances = dict()
    for line in puzzle_input.split('\n'):
        x, y, z = map(int, line.split(','))
        boxes.append((x, y, z))
    for a, b in tqdm(combinations(boxes, 2)):
        dist = distance_3d_nosqrt(a, b)
        distances[(a, b)] = dist
        # distances[(b, a)] = dist
    return boxes, distances

from collections import deque

def part1(data):
    """Solve part 1"""
    boxes, distances = data
    sdist = deque(sorted(distances.items(), key=lambda item: item[1]))
    circuits = []
    
    # Connect closest pairs for 1000 iterations
    for i in tqdm(range(1000)):
        pair = sdist.popleft()
        a, b = pair[0]
        
        # Find which circuits contain a or b
        circuit_indices = [n for n, c in enumerate(circuits) if a in c or b in c]
        
        if not circuit_indices:
            # Neither a nor b in any circuit, create new one
            circuits.append({a, b})
        elif len(circuit_indices) == 1:
            # Add both to the existing circuit
            circuits[circuit_indices[0]].add(a)
            circuits[circuit_indices[0]].add(b)
        else:
            # a and b are in different circuits, merge them
            merged = {a, b}
            for idx in sorted(circuit_indices, reverse=True):
                merged |= circuits[idx]
                circuits.pop(idx)
            circuits.append(merged)
    
    # Sort by size and return product of three largest
    circuits.sort(key=len, reverse=True)
    return len(circuits[0]) * len(circuits[1]) * len(circuits[2]), data

def part2(data):
    """Solve part 2 - find the last pair that unites all boxes into one circuit"""
    boxes, distances = data
    # Start fresh from beginning of sorted distances
    sdist = deque(sorted(distances.items(), key=lambda item: item[1]))
    
    # Initialize each box in its own circuit
    circuits = [{box} for box in boxes]
    last_merged_pair = None
    
    while len(circuits) > 1 and sdist:
        pair = sdist.popleft()
        a, b = pair[0]
        
        # Find which circuits contain a or b
        circuit_indices = [n for n, c in enumerate(circuits) if a in c or b in c]
        
        if len(circuit_indices) == 2:
            # a and b are in different circuits, merge them
            i, j = sorted(circuit_indices, reverse=True)
            circuits[i] |= circuits[j]
            circuits.pop(j)
            last_merged_pair = pair  # Track this merge
        elif len(circuit_indices) == 1:
            # One is in a circuit, add the other to it
            circuits[circuit_indices[0]].add(a)
            circuits[circuit_indices[0]].add(b)
        else:
            # Neither in any circuit, create new one (shouldn't happen with init)
            circuits.append({a, b})
    
    # Return product of X coordinates of last merged pair
    return last_merged_pair[0][0][0] * last_merged_pair[0][1][0]

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        data = process(puzzle_input)

        solution1, _ = part1(data)
        print("PART1:", solution1)

        solution2 = part2(data)
        print("PART2:", solution2)