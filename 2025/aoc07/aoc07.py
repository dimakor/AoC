import pathlib
import sys
from rich import print
from functools import lru_cache


def process(puzzle_input):
    """Parse input"""
    manifold = []
    for line in puzzle_input.split('\n'):
        manifold.append(line)
    return manifold

def part1(data):
    """Solve part 1"""
    splits = 0
    p = {data[0].index('S')} # find start poisition of beam
    # print("START POSITIONS:", p)
    for m in data[2:]:
        if m.find('^') == -1:
            continue
        beams = list(p)
        p = set()
        for beam in beams:
            if m[beam] == '.':
                p.add(beam)
            elif m[beam] == '^':
                p.add(beam - 1)
                p.add(beam + 1)
                splits += 1
        # print("BEAM POSITIONS:", p, "splits:", splits)
    return splits

def count_paths(graph, root):
    @lru_cache(maxsize=None)
    def dfs(node):
        if node not in graph or not graph[node]:
            return 1  # Leaf node
        total_paths = 0
        for neighbor in graph[node]:
            total_paths += dfs(neighbor)
        return total_paths
    return dfs(root)

def part2(data):
    """Solve part 2"""
    splits = 0
    root = (0, data[0].index('S')) # find start poisition of beam
    graph = {}
    p = [root]
    for h, m in enumerate(data):
        if m.find('^') == -1 or h == 0:
            continue
        nextlevel = set()
        for beam in p:
            children = []
            if m[beam[1]] == '.':
                children += [(h, beam[1])]
                nextlevel.add((h, beam[1]))
            elif m[beam[1]] == '^':
                children += [(h, beam[1] - 1)]
                children += [(h, beam[1] + 1)]
                nextlevel.add((h, beam[1] - 1))
                nextlevel.add((h, beam[1] + 1))
            graph[beam] = children
        p = nextlevel.copy()
    return count_paths(graph, root)

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        data = process(puzzle_input)

        solution1 = part1(data)
        print("PART1:", solution1)

        solution2 = part2(data)
        print("PART2:", solution2)