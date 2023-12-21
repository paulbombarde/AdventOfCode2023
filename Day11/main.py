def solve(path, expansion_factor):
    map = parse(path)

    els = empty_lines(map)
    ecs = empty_columns(map)
    gs = galaxies(map)

    s = 0
    for i in range(len(gs)):
        for j in range(i+1, len(gs)):
            xmin = min(gs[i][0], gs[j][0])
            xmax = max(gs[i][0], gs[j][0])
            ymin = min(gs[i][1], gs[j][1])
            ymax = max(gs[i][1], gs[j][1])

            d = xmax - xmin + ymax - ymin
            for el in els:
                if xmin < el < xmax:
                    d += expansion_factor - 1

            for ec in ecs:
                if ymin < ec < ymax:
                    d += expansion_factor - 1

            s+= d

    return s


def parse(path):
    with open(path) as file:
        return [l.rstrip() for l in file]

def empty_lines(map):
    return {i for i,l in enumerate(map) if empty_line(l)}


def empty_line(l):
    for c in l:
        if c == "#":
            return False
    return True


def empty_columns(map):
    return {j for j in range(len(map[0])) if empty_column(map, j)}


def empty_column(map, j):
    for l in map:
        if l[j] == "#":
            return False
    return True


def galaxies(map):
    return [g for g in igalaxies(map)]


def igalaxies(map):
    for i,l in enumerate(map):
        for j,c in enumerate(l):
            if map[i][j] == "#":
                yield i,j


if __name__ == "__main__":
    print(solve('sample', 2))
    print(solve('input', 2))
    print(solve('sample', 10))
    print(solve('sample', 100))
    print(solve('input', 1000000))
