import pathlib
import sys
from rich import print
import parse
import networkx as nx

OP = {
    "AND": lambda x, y: x & y,
    "OR": lambda x, y: x | y,
    "XOR": lambda x, y: x ^ y,
}

def calc(node : list, nodes_values):
    return OP[node[2]](nodes_values[node[0]], nodes_values[node[1]])

def process(puzzle_input):
    """Parse input"""
    inp = True
    nodes_values = dict()
    node_string = parse.compile("{} {} {} -> {}")
    nodes = dict()  # [i1, i2, op]
    for line in puzzle_input.split("\n"):
        if inp:
            # input values part
            if line == "":
                inp = False
                continue
            nodes_values[line[:3]] = int(line[5:])
        else:
            p = node_string.parse(line)
            nodes[p[3]] = [p[0], p[2], p[1]]
    # print(nodes_values)
    # print(nodes)
    return nodes, nodes_values


def part1(data):
    """Solve part 1"""
    nodes, nodes_values = data
    fin = True
    while fin:
        fin = False
        for node in nodes:
            if node in nodes_values:
                continue
            fin = True
            prop = nodes[node]
            if prop[0] in nodes_values and prop[1] in nodes_values:
                nodes_values[node] = calc(prop, nodes_values)
    res = []
    for i in nodes_values:
        if i[0] == 'z':
            res.append(i)
    res.sort()
    res.reverse()
    res2 = map(lambda x: str(nodes_values[x]), res)
    result = ''.join(res2)
    print("Z:", result)
    return int(result, 2), result

def toBinary(startchar, nodes_values):
    res = []
    for i in nodes_values:
        if i[0] == startchar:
            res.append(i)
    res.sort()
    res.reverse()
    res2 = map(lambda x: str(nodes_values[x]), res)
    result = ''.join(res2)
    return result

def part2(data, Z):
    """Solve part 2"""
    nodes, nodes_values = data
    x = toBinary('x', nodes_values)
    y = toBinary('y', nodes_values)
    print(x, int(x,2))
    print(y, int(y,2))
    rz = int(x,2)+ int(y,2)
    print("Z*:", format(rz, '10b'), rz)
    print("Z :", format(int(Z, 2), '10b'), int(Z, 2))



if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        data = process(puzzle_input)
        solution1, Z = part1(data)
        solution2 = part2(data, Z)
        print("PART1:", solution1)
        print("PART2:", solution2)
