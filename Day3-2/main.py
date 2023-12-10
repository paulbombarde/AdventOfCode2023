from collections import defaultdict
def solve(path):
    gears, numbers = parse(path)
    nums = defaultdict(list)
    for i,b,e,v in numbers:
        nums[i].append((b,e,v))

    res = 0
    for i,l in enumerate(gears):
        for j in l:
            res += ratio(nums, i, j)
    return res


def ratio(nums, i, j):
    ns = get_nums(nums[i-1], j) + get_nums(nums[i+1], j)
    for b,e,v in nums[i]:
        if b == j or e == j:
            ns.append(v)
    if len(ns) != 2:
        return 0
    return ns[0]*ns[1]


def get_nums(nums, j):
    return [v for b,e,v in nums if b <= j <= e]

def parse(path):
    numbers = []
    gears = []
    with open(path) as file:
        for i,l in enumerate(file):
            s, n = parse_line(i, l.strip())
            gears.append(s)
            numbers = numbers + n
    return gears, numbers


def parse_line(i, l):
    numbers = []
    gears = []
    j=0
    while j<len(l):
        if l[j] == "*":
            gears.append(j)
            j+=1
            continue

        if not l[j].isdigit():
            j+=1
            continue

        v=0
        b=j-1
        while j<len(l):
            if not l[j].isdigit():
                numbers.append((i,b,j, v))
                break

            v= v*10 + int(l[j])
            j+=1
        if j == len(l):
            numbers.append((i, b, j, v))

    return gears, numbers


if __name__ == '__main__':
    print(solve("/Users/logi/Repositories/AdventOfCode2023/Day3-2/input"))