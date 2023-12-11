def solve(path):
    with open(path) as file:
        wins = [points(l) for l in file]

    cards = [1] * len(wins)
    for i in range(len(wins)):
        for j in range(i + 1, i + wins[i] + 1):
            cards[j] += cards[i]

    return sum(cards)


def points(line):
    _, v = line.split(": ")
    wins, haves = v.split(" | ")
    wins = set((int(s) for s in wins.split(" ") if s))
    haves = set((int(s) for s in haves.split(" ") if s))
    both = wins.intersection(haves)
    return len(both)


if __name__ == '__main__':
    print(solve("/Users/logi/Repositories/AdventOfCode2023/Day4-1/input"))
