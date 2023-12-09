def solve(path):
    symbols, numbers = parse(path)
    print(numbers)
    print(symbols)
    res = 0
    for i,b,e,v in numbers:
        if has_symbol(symbols, i, b-1, e):
            res += v
            print(v, "valid")
        else:
            print(v, "no valid")
    return res


def has_symbol(symbols, i, b, e):
    if 0 < i and has_symbol_line(symbols[i-1], b, e):
        return True
    if i < len(symbols)-1 and has_symbol_line(symbols[i+1], b, e):
        return True
    if b in symbols[i] or e in symbols[i]:
        return True
    return False


def has_symbol_line(symbols, b, e):
    for s in symbols:
        if b <= s <= e:
            return True
    return False

def parse(path):
    numbers = []
    symbols = []
    with open(path) as file:
        for i,l in enumerate(file):
            s, n = parse_line(i, l.strip())
            symbols.append(s)
            numbers = numbers + n
    return symbols, numbers


def parse_line(i, l):
    numbers = []
    symbols = []
    j=0
    while j<len(l):
        if l[j] == ".":
            j+=1
            continue

        if not l[j].isdigit():
            symbols.append(j)
            j+=1
            continue

        v=0
        b=j
        while j<len(l):
            if not l[j].isdigit():
                numbers.append((i,b,j, v))
                break

            v= v*10 + int(l[j])
            j+=1
        if j == len(l):
            numbers.append((i, b, j, v))

    return symbols, numbers


if __name__ == '__main__':
    print(solve("/Users/logi/Repositories/AdventOfCode2023/Day3-1/input"))