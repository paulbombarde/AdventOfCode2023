from math import lcm
def solve(path):
    instructions, map = parse(path)
    r = "AAA"
    c = 0
    while r != "ZZZ":
        i = 0 if instructions[c % len(instructions)] == "L" else 1
        r = map[r][i]
        c += 1

    return c


def solve2(path):
    instructions, map = parse(path)
    l = len(instructions)
    nodes = [n for n in map if n[-1] == "A"]

    factors = set()
    for i in range(len(nodes)):
        c = 0
        node = nodes[i]
        for a in range(len(map)):
            while node[-1] != "Z":
                j = 0 if instructions[c % l] == "L" else 1
                node = map[node][j]
                c += 1
            factors.add(c)

    return lcm(*factors)

def all_endz(nodes):
    for n in nodes:
        if n[-1] != "Z":
            return False
    return True

def one_ends(nodes):
    for n in nodes:
        if n[-1] == "Z":
            return True
    return False


def parse(path):
    with open(path) as file:
        lines = iter(file)
        instructions = next(lines).rstrip()
        next(lines) # white line
        map = {l[0:3]:(l[7:10], l[12:15]) for l in lines}

    return instructions, map


if __name__ == "__main__":
    print(solve("/Users/logi/Repositories/AdventOfCode2023/Day8/sample1"))
    print(solve("/Users/logi/Repositories/AdventOfCode2023/Day8/sample2"))
    print(solve("/Users/logi/Repositories/AdventOfCode2023/Day8/input"))
    print(solve2("/Users/logi/Repositories/AdventOfCode2023/Day8/sample3"))
    print(solve2("/Users/logi/Repositories/AdventOfCode2023/Day8/input"))
