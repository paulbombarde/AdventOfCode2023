from collections import defaultdict
from functools import cmp_to_key



def solve(path, type, cmp):
    games = [g for g in parse(path)]
    #print(games)

    typed_games = defaultdict(list)
    for g in games:
        typed_games[type(g[0])].append(g)
    #print(typed_games)

    sorted_games = []
    for k in sorted(typed_games.keys()):
        sorted_games += sorted(typed_games[k], key=cmp_to_key(cmp))
    #print(sorted_games)

    return sum(g[1]*i for i,g in enumerate(sorted_games, start=1))


def parse(path):
    with open(path) as file:
        for l in file:
            hand, bid = l.rstrip().split(' ')
            yield hand, int(bid)


score1 = {
    "A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "9": 9,
    "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2
}

score2 = {
    "A": 14, "K": 13, "Q": 12, "J": 1, "T": 10, "9": 9,
    "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2
}

def compare1(g1, g2):
    return compare(g1, g2, score1)

def compare2(g1, g2):
    return compare(g1, g2, score2)

def compare(g1, g2, score):
    h1 = g1[0]
    h2 = g2[0]
    for p in range(5):
        if score[h1[p]] == score[h2[p]]:
            continue
        return -1 if score[h1[p]] < score[h2[p]] else 1
    return 0


# 6 => 5 of a kind
# 5 => 4 of a kind
# 4 => full
# 3 => 3 of a kind
# 2 => 2 pairs
# 1 => 1 pair
# 0 => all diff
def type1(hand):
    d = defaultdict(int)
    for c in hand:
        d[c] += 1

    s = sorted((n for l,n in d.items()))
    if s[-1] == 5:
        return 6
    if s[-1] == 4:
        return 5
    if s[-1] == 3:
        return 4 if s[-2] == 2 else 3
    if s[-1] == 2:
        return 2 if s[-2] == 2 else 1
    return 0

def type10(hand):
    h = sorted(hand)
    if h[0] == h[1]:
        # one pair
        if h[1] == h[2]:
            # at least 3 same
            if h[2] == h[3]:
                # at least 4 same
                return 6 if h[3] == h[4] else 5
            else:
                return 4 if h[3] == h[4] else 3
        elif h[2] == h[3]:
            # 2 pairs
            return 4 if h[3] == h[4] else 2
        else:
            return 2 if h[3] == h[4] else 1
    elif h[1] == h[2]:
        # one pair
        if h[2] == h[3]:
            # at least 3 same
            return 5 if h[3] == h[4] else 3
        else:
            return 2 if h[3] == h[4] else 1
    elif h[2] == h[3]:
        # one pair
        return 3 if h[3] == h[4] else 1
    else:
        return 1 if h[3] == h[4] else 0


def type2(hand):
    d = defaultdict(int)
    for c in hand:
        d[c] += 1

    dj = d['J']
    if dj == 5 or dj == 4:
        return 6
    del d['J']

    s = sorted((n for l,n in d.items()))
    s[-1] += dj
    if s[-1] == 5:
        return 6
    if s[-1] == 4:
        return 5
    if s[-1] == 3:
        return 4 if s[-2] == 2 else 3
    if s[-1] == 2:
        return 2 if s[-2] == 2 else 1
    return 0

def solve1(path):
    return solve(path, type1, compare1)

def solve2(path):
    return solve(path, type2, compare2)

if __name__ == "__main__":
    print(solve1("/Users/logi/Repositories/AdventOfCode2023/Day7/sample"))
    print(solve1("/Users/logi/Repositories/AdventOfCode2023/Day7/input"))
    print(solve2("/Users/logi/Repositories/AdventOfCode2023/Day7/sample"))
    print(solve2("/Users/logi/Repositories/AdventOfCode2023/Day7/input"))
