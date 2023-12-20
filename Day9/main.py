def solve(path):
    with open(path) as file:
        return sum(extrapolate_back(build_diffs(l.rstrip())) for l in file)


def solve2(path):
    with open(path) as file:
        return sum(extrapolate_front(build_diffs(l.rstrip())) for l in file)


def build_diffs(l):
    vals = [[int(n) for n in l.split(' ')]]
    while not all_zeros(vals[-1]):
        vals.append(diffs(vals[-1]))
    return vals


def extrapolate_back(vals):
    vals[-1].append(0)
    for i in range(len(vals)-2, -1, -1):
        vals[i].append(vals[i+1][-1] + vals[i][-1])

    return vals[0][-1]


def extrapolate_front(vals):
    # put the new front value at the back
    vals[-1].append(0)
    for i in range(len(vals)-2, -1, -1):
        vals[i].append(vals[i][0] - vals[i+1][-1])

    return vals[0][-1]


def all_zeros(vals):
    for v in vals:
        if v != 0:
            return False
    return True


def diffs(vals):
    return [vals[i] - vals[i-1] for i in range(1, len(vals))]


if __name__ == "__main__":
    print(solve('sample'))
    print(solve('input'))
    print(solve2('sample'))
    print(solve2('input'))
