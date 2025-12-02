import time
from operator import itemgetter

""" Advent of Code solver class """
startparse = time.time()
with open('input.txt', 'r', encoding='utf8') as file_handle:
    inp = [[x for x in line.strip()] for line in file_handle]

maxr = len(inp)
maxc = len(inp[0])
plots = {} # contains id : "char"
coords = {} # contains id : set((r1, c1), (r2, c2))...
fences = {} # contains id : dict full of directions that contain each panel on that side

endparse = time.time()
print(f"Parsing took {(endparse-startparse)*10**3:.03f}ms")

def getPlotID(char, r, c):
    for id, val in plots.items():
        if val == char:
            if (r, c) in coords[id]:
                return id
    return -1

def mapPlot(plotid, row, col):
    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        if 0 <= row+dr < maxr and 0 <= col+dc < maxc and inp[row+dr][col+dc] == inp[row][col]:
            if (row+dr, col+dc) not in coords[plotid]:
                coords[plotid].add((row+dr, col+dc))
                mapPlot(plotid, row+dr, col+dc)
            continue
        if plotid in fences:
            fences[plotid][dr,dc].add((row, col))
        else:
            fences[plotid] = {(1, 0): set(), (0, 1): set(), (-1, 0): set(), (0, -1): set()}
            fences[plotid][dr,dc].add((row, col))

def task1():
    """ Task 1 solver """
    for row, line in enumerate(inp):
        for col, plot in enumerate(line):
            plotid = getPlotID(plot, row, col)
            if plotid >= 0:
                continue
            plotid = len(plots)
            plots[plotid] = plot
            coords[plotid] = set()
            coords[plotid].add((row, col))
            mapPlot(plotid, row, col)

    cost = 0
    for id, panels in fences.items():
        for dir in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            cost += len(panels[dir]) * len(coords[id])
        #print("(Region id", id, ") char", plots[id], "plants with price", len(coords[id]), "*", panels, "+",len(coords[id]) * panels)
    return cost

start = time.time()
print("Task 1 result:", task1(), f" (time: {(time.time()-start)*10**3:.03f}ms)")

def task2():
    """ Task 2 solver """
    cost = 0
    for id, fencepanels in fences.items():
        sides = 0
        for dir in fencepanels:
            prev = (-1, -1)

            # horizontal fence panels
            if dir == (1, 0) or dir == (-1, 0):
                for _, panel in enumerate(sorted(fencepanels[dir],key=itemgetter(0, 1))):
                    sides += 1
                    if prev != (-1, -1) and panel[1] == prev[1]+1 and panel[0] == prev[0]:
                        sides -= 1
                    prev = panel

            # vertical fence panels
            if dir == (0, 1) or dir == (0, -1):
                for _, panel in enumerate(sorted(fencepanels[dir],key=itemgetter(1, 0))):
                    sides += 1
                    if prev != (-1, -1) and panel[0] == prev[0]+1 and panel[1] == prev[1]:
                        sides -= 1
                    prev = panel

        cost += sides * len(coords[id])
    return cost

# sample2 = 80
# sample3 = 436
# sample4 = 236
# sample5 = 368

start = time.time()
print("Task 2 result:", task2(), f" (time: {(time.time()-start)*10**3:.03f}ms)")