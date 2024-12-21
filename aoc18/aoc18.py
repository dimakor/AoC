import pathlib
import sys
from rich import print

import heapq
import tqdm

SIZE = 70 + 1
BYTES = 1024

DIR = {'E': ['N', 'S'],
       'W' : ['N', 'S'],
       'N' : ['E', 'W'],
       'S' : ['E', 'W'],}
SIDE = {(1, 0) : 'S', (-1, 0) : 'N', (0, -1): 'W', (0, 1):'E'}

class PriorityQueue:
    def __init__(self):
        self.elements  = []
    
    def empty(self):
        return not self.elements
    
    def put(self, item, priority: float):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]

def cost(current, next):
    s = SIDE[next]
    if current[1] == s:
        return 1
    if current[1] in DIR[s]:
        return 1001
    return 2001

def printmaze(maze):
    for line in maze:
        print(''.join(line))

def h(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2) # make one turn

def neighbors(maze, p):
    pos = p #only location, no direction
    nbors = []
    for n in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
        ny = pos[0] + n[0]
        nx = pos[1] + n[1]
        if (nx < 0) or (nx>= SIZE) or (ny <0) or (ny >= SIZE):
            continue
        # print("NX, NY", nx, ny)
        if maze[ny][nx] != "#":
            nbors.append(n)
    return nbors

def a_star_search(maze, start, goal):
    frontier = PriorityQueue()
    frontier.put((start), 0)
    came_from: dict = {}
    cost_so_far: dict = {}
    came_from[(start)] = None
    cost_so_far[(start)] = 0
    
    while not frontier.empty():
        current = frontier.get()
        
        if current == goal:
            break
        
        for next in neighbors(maze, current):
            new_cost = cost_so_far[current] + 1 #cost(current, next)
            nextpos = (current[0]+next[0], current[1] +next[1])
            if nextpos not in cost_so_far or new_cost < cost_so_far[nextpos]:
                cost_so_far[nextpos] = new_cost
                priority = new_cost + h(nextpos, goal)
                frontier.put(nextpos, priority)
                came_from[nextpos] = current
    
    return came_from, cost_so_far

def process(puzzle_input, a = 0):
    """Parse input"""
    maze = [['.' for i in range(SIZE)] for j in range(SIZE)] 
    n = 0
    for line in puzzle_input.split('\n'):
        if n == BYTES + a:
            break
        i = line.index(',')
        x = int(line[:i])
        y = int(line[i+1:])
        maze[y][x] = '#'
        n += 1
    if a > 0:
        return maze, (x,y)
    return maze

def part1(data):
    """Solve part 1"""
    END = (SIZE-1, SIZE-1)
    print(data)
    came_from, cost_so_far = a_star_search(data, (0,0), END)
    p = END
    count = 0
    while p!=(0,0):
        p = came_from[p]
        count +=1
    return(count)

def part2(data):
    """Solve part 2"""
    END = (SIZE-1, SIZE-1)
    for i in tqdm.tqdm(range(1, 3450-1024)):
        maze, block = process(data, i)
        came_from, cost_so_far = a_star_search(maze, (0,0), END)
        try:
            came_from[END]
        except KeyError:
            return block
    return None
        

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        data = process(puzzle_input)
        # solution1 = part1(data)
        solution2 = part2(puzzle_input)
        # print("PART1:", solution1)
        print("PART2:", solution2)

