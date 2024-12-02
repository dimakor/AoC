import pathlib
import sys
#from rich import print
import parse
from collections import namedtuple
import numpy as np

Point = namedtuple("Point", "x y")
Node = namedtuple("Node", "p previous")

def process(puzzle_input):
    """Parse input"""
    map = []
    
    for y, line in enumerate(puzzle_input.split('\n')):
        map.append(line)
        x = line.find('S')
        xe = line.find('E')
        if  x != -1:
            S = Point(x, y)
        if  xe != -1:
            E = Point(xe, y)

    return S, E, map

def get_adjacent_nodes(map, node):
    move = [[+1, 0], [-1, 0], [0, +1], [0, -1]]
    h = ord('a') if map[node.y][node.x] == 'S' else ord(map[node.y][node.x]) 
    msize = Point(len(map[0]), len(map))
    adj = []
    for i in move:
        try:
            a = Point(node.x + i[0], node.y + i[1])
            if (a.x <0 ) or (a.y<0):
                continue
            hnew = ord('z') if map[a.y][a.x] == 'E' else ord(map[a.y][a.x])
            if (hnew - h) <= 1:
                adj.append(a)
        except:
            pass
    return adj

def choose_node(cost, reachable):
    best_node = None

    for node in reachable:
        if best_node == None or cost.get(best_node, 1000000) > cost.get(node, 1000000):
            best_node = node
    
    return best_node

def part1(data):
    """Solve part 1"""
    S = data[0]
    E = data[1]
    map = data[2]
    msize = Point(len(map[0]), len(map))
    #v = np.zeros(shape = (msize.x, msize.y))
    #v[S.x][S.y] = 1 # visited start
    reachable = [S]
    rdict = {}
    explored = []
    cost = {S: 0}
    while reachable:
        node = choose_node(cost, reachable) #TODO:
        if node == E:
            path = []
            while node != S:
                path.append(node)
                node = rdict[node]
            return path
        reachable.remove(node)
        explored.append(node)

        new_reachable = get_adjacent_nodes(map, node) 
        for e in explored:
            try:
                new_reachable.remove(e)
            except:
                pass
        for r in new_reachable:
            if r not in reachable:
                #rdict[r] = node  # Remember how we got there.
                reachable.append(r)
                # If this is a new path, or a shorter path than what we have, keep it.
                if cost.get(node, 1000000) + 1 < cost.get(r,1000000):
                    rdict[r] = node
                    cost[r] = cost.get(node, 1000000) + 1
    return None

def part2(data):
    """Solve part 2"""
    S = data[0]
    E = data[1]
    map = data[2]
    msize = Point(len(map[0]), len(map))
    #for i in range(5, msize):
    alla = []
        # Ex +i, Ex-i, Ey+i, Ey-i
        #nmap = [ map[j][E.x-i:E.x+i] for j in range(E.y-i, E.y+i)]
    nmap =map
        #print (nmap)
    for ay, line in enumerate(nmap):
        for ii in find_all(line):
            route = findroute([Point(x=ii, y=ay), E, nmap])
            if route:
                alla.append(len(route))
                print(route)
    return min(alla)

def find_all(line):
    i = line.find('a')
    ret = []
    while i != -1:
        ret.append(i)
        i = line.find('a', i+1)
    return ret

def findroute(data):
    """Solve part 1"""
    S = data[0]
    E = data[1]
    map = data[2]
    msize = Point(len(map[0]), len(map))
    #v = np.zeros(shape = (msize.x, msize.y))
    #v[S.x][S.y] = 1 # visited start
    reachable = [S]
    rdict = {}
    explored = []
    cost = {S: 0}
    while reachable:
        node = choose_node(cost, reachable) #TODO:
        if node == E:
            path = []
            while node != S:
                path.append(node)
                node = rdict[node]
            return path
        reachable.remove(node)
        explored.append(node)

        new_reachable = get_adjacent_nodes(map, node) 
        for e in explored:
            try:
                new_reachable.remove(e)
            except:
                pass
        for r in new_reachable:
            if r not in reachable:
                #rdict[r] = node  # Remember how we got there.
                reachable.append(r)
                # If this is a new path, or a shorter path than what we have, keep it.
                if cost.get(node, 1000000) + 1 < cost.get(r,1000000):
                    rdict[r] = node
                    cost[r] = cost.get(node, 1000000) + 1
    return None

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        data = process(puzzle_input)
        #solution1 = part1(data)
        solution2 = part2(data)
        #print("PART1:", len(solution1))
        print("PART2:", solution2)