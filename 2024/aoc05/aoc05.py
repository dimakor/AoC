import pathlib
import sys
from rich import print

def process(puzzle_input):
    """Parse input"""
    updates_section = False
    rules = []
    updates = []
    for line in puzzle_input.split('\n'):
        if line == "":
            updates_section = True
            continue
        if not updates_section:
            sep = line.index('|')
            rules.append((line[:sep], line[sep+1:]))
        if updates_section:
            updates.append(line.split(','))
    return (rules, updates)

        

def part1(data):
    """Solve part 1"""
    rules, updates = data
    res = 0
    incorrect = []
    for update in updates:
        correct = True
        for r in rules:
            try:
                if update.index(r[0]) >= update.index(r[1]):
                    correct = False
            except ValueError:
                pass
        if correct:
            # print(update)
            ind = int((len(update)-1)/2)
            page = int(update[ind])
            # print("IND:", ind, " PAGE:", page)
            res += page
        else:
            incorrect.append(update)
    return res, incorrect

def check(rules, update):
    correct = True
    for r in rules:
        try:
            if update.index(r[0]) >= update.index(r[1]):
                correct = False
        except ValueError:
            pass
    return correct

def part2(data):
    """Solve part 2"""
    rules, incorrect = data
    res = 0
    for i in incorrect:
        while not check(rules, i):
            for r in rules:
                try:
                    if i.index(r[0]) >= i.index(r[1]):
                        a = i.index(r[0])
                        b = i.index(r[1])
                        i[a], i [b] = i[b], i[a]
                except ValueError:
                    pass
        ind = int((len(i)-1)/2)
        page = int(i[ind])
        # print("IND:", ind, " PAGE:", page)
        res += page 
    return res

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        data = process(puzzle_input)
        solution1, incorrect = part1(data)
        solution2 = part2((data[0], incorrect))
        print("PART1:", solution1)
        print("PART2:", solution2)