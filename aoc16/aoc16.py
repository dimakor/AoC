import pathlib
import sys
from rich import print
import heapq
from collections import defaultdict
import math

def process(puzzle_input):
    """Parse input"""
    maze = []
    for line in puzzle_input.split('\n'):
        maze.append(list(line))
    return maze
        

def part1(maze):
    """Solve part 1"""
    Y = len(maze)
    X= len(maze[0])
    S = (Y - 2, 1)
    E = (1, X - 2)
    came_from, cost_so_far = a_star_search(maze, S, E)
    for p, val in cost_so_far.items():
        if p[0] == E:
            return val

def part2(maze):
    """Solve part 2"""
    Y = len(maze)
    X= len(maze[0])
    S = (Y - 2, 1)
    E = (1, X - 2)
    came_from, cost_so_far = a_star_search2(maze, E, S)
    p = set()
    for i in came_from:
        p.add(i[0])
    return len(p)
    

def printmaze(maze):
    for line in maze:
        print(''.join(line))

def h(a, b):
    (x1, y1) = a[0]
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2) + 1000 # make one turn

def neighbors(maze, p):
    pos = p[0] #only location, no direction
    nbors = []
    for n in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
        if maze[pos[0] + n[0]][pos[1] + n[1]] != "#":
            nbors.append(n)
    return nbors

def a_star_search(maze, start, goal):
    frontier = PriorityQueue()
    frontier.put((start, 'E'), 0)
    came_from: dict = {}
    cost_so_far: dict = {}
    came_from[(start, 'E')] = None
    cost_so_far[(start, 'E')] = 0
    
    while not frontier.empty():
        current = frontier.get()
        
        if current == goal:
            break
        
        for next in neighbors(maze, current):
            new_cost = cost_so_far[current] + cost(current, next)
            nextpos = ((current[0][0]+next[0], current[0][1] +next[1]), SIDE[next])
            if nextpos not in cost_so_far or new_cost < cost_so_far[nextpos]:
                cost_so_far[nextpos] = new_cost
                priority = new_cost + h(nextpos, goal)
                frontier.put(nextpos, priority)
                came_from[nextpos] = current
    
    return came_from, cost_so_far

def a_star_search2(maze, start, goal):
    scores = defaultdict(lambda: math.inf)
    res = math.inf

    frontier = PriorityQueue()
    frontier.put((start, 'E'), 0)
    came_from: dict = {}
    cost_so_far: dict = {}
    came_from[(start, 'E')] = None
    cost_so_far[(start, 'E')] = 0
    all_tiles = set()
    
    while not frontier.empty():
        current = frontier.get()
        
        if current[0] == goal:
            res = min(res, cost_so_far[current])
            if cost_so_far[current] == res:
                all_tiles.add(current[0])
        
        for next in neighbors(maze, current):
            new_cost = cost_so_far[current] + cost(current, next)
            nextpos = ((current[0][0]+next[0], current[0][1] +next[1]), SIDE[next])
            if nextpos not in cost_so_far or new_cost <= cost_so_far[nextpos]:
                cost_so_far[nextpos] = new_cost
                priority = new_cost + h(nextpos, goal)
                frontier.put(nextpos, priority)
                came_from[nextpos] = current
    
    return came_from, cost_so_far

DIR = {'E': ['N', 'S'],
       'W' : ['N', 'S'],
       'N' : ['E', 'W'],
       'S' : ['E', 'W'],}
SIDE = {(1, 0) : 'S', (-1, 0) : 'N', (0, -1): 'W', (0, 1):'E'}

def cost(current, next):
    s = SIDE[next]
    if current[1] == s:
        return 1
    if current[1] in DIR[s]:
        return 1001
    return 2001
    
class PriorityQueue:
    def __init__(self):
        self.elements  = []
    
    def empty(self):
        return not self.elements
    
    def put(self, item, priority: float):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]
    
if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        data = process(puzzle_input)
        solution1 = part1(data)
        solution2 = part2(data)
        print("PART1:", solution1)
        print("PART2:", solution2)