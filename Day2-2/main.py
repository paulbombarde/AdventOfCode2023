def solve(path):
    with open(path) as file:
        return sum(power(l.strip()) for l in file)


def power(line):
    i, maxs = maxes(line)
    return maxs["red"] * maxs["green"] * maxs["blue"]


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
    print(solve("/Users/logi/Repositories/AdventOfCode2023/Day2-2/input"))
