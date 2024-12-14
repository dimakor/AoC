import pathlib
import sys
from rich import print
import parse
import numpy as np
from PIL import Image


def process(puzzle_input):
    """Parse input"""
    prg = parse.compile("p={},{} v={},{}")
    P = []
    V = []
    for line in puzzle_input.split("\n"):
        res = prg.parse(line)
        P.append((int(res[0]), int(res[1])))
        V.append((int(res[2]), int(res[3])))
    return P, V


def part1(data):
    """Solve part 1"""
    # size of bathroom
    X = 101
    Y = 103
    QX = (X-1) / 2
    QY = (Y-1) / 2
    SECONDS = 100
    P, V = data
    SAFETY = []
    for i in range(10000):
        #image_array = np.zeros((X+5, Y+5, 3), dtype=np.uint8)
        q1 = q2 = q3 = q4 = 0
        for p, v in zip(P, V):
            x = (p[0] + v[0] * i) % X
            y = (p[1] + v[1] * i) % Y
            # print("X, Y:", x, y)
            #image_array[y, x] = 255
            if x < QX and y < QY:
                q1 += 1
            if x > QX and y < QY:
                q2 += 1
            if x < QX and y > QY:
                q3 += 1
            if x > QX and y > QY:
                q4 += 1
        #image = Image.fromarray(image_array)
        #image.save('img\output'+str(i)+'.png')  # Save the image
        SAFETY.append((q1 * q2 * q3 * q4, i))
    return q1 * q2 * q3 * q4, SAFETY



def part2(data):
    """Solve part 2"""
    data.sort(key = lambda a: a[0])
    for i in range(10):
        print(data[i])
    return data[0][1]


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        data = process(puzzle_input)
        solution1, SAFETY = part1(data)
        solution2 = part2(SAFETY)
        print("PART1:", solution1)
        print("PART2:", solution2)
