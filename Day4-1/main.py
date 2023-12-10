def solve(path):
    with open(path) as file:
        return sum(points(l) for l in file)

def points(line):
    _,v = line.split(": ")
    wins,haves = v.split(" | ")
    wins = set((int(s) for s in wins.split(" ") if s))
    haves = set((int(s) for s in haves.split(" ") if s))
    both = wins.intersection(haves)
    if not both:
        return 0
    return pow(2, len(both)-1)


if __name__ == '__main__':
    print(solve("/Users/logi/Repositories/AdventOfCode2023/Day4-1/input"))
