def solve(path):
    with open(path) as file:
        return sum(valid(l.strip()) for l in file)


def valid(line):
    i, maxs = maxes(line)
    if maxs["red"] <= 12 and maxs["green"] <= 13 and maxs["blue"] <= 14:
        return i
    return 0


def maxes(line):
    game, draws = line.split(": ")
    draws = draws.split('; ')
    maxs = {"red": 0, "green": 0, "blue": 0}
    for draw in draws:
        vals = draw.split(", ")
        for val in vals:
            v, c = val.split(" ")
            maxs[c] = max(maxs[c], int(v))
    return int(game[5:]), maxs


if __name__ == '__main__':
    print(solve("/Users/logi/Repositories/AdventOfCode2023/Day2-1/input"))
