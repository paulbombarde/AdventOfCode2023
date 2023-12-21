from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])


def solve(path):
    S, map = parse(path)

    tracks = [[S, p] for p in find_firsts(S, map)]
    while tracks[0][-1] != tracks[1][-1]:
        for t in tracks:
            t.append(next_point(t, map))

    return len(tracks[0])-1


def solve2(path):
    S, map = parse(path)

    starts = [p for p in find_firsts(S, map)]
    if starts[0].x == starts[1].x:
        map[S.x][S.y] = '-'
    elif starts[0].y == starts[1].y:
        map[S.x][S.y] = '|'
    elif starts[0].y < starts[1].y:
        if starts[0].x < starts[1].x:
            map[S.x][S.y] = 'L'
        else:
            map[S.x][S.y] = 'F'
    else:
        if starts[0].x < starts[1].x:
            map[S.x][S.y] = 'J'
        else:
            map[S.x][S.y] = '7'

    track = [S, starts[0]]
    while track[-1] != S:
        track.append(next_point(track, map))
    on_track = { p for p in track}

    c = 0
    for i,l in enumerate(map):
        inside = None
        for j,v in enumerate(l):
            if not Point(i,j) in on_track:
                if inside:
                    map[i][j] = "I"
                    c+=1
                else:
                    map[i][j] = "0"
                continue

            if v in ['|', 'F', '7']:
                inside = None if inside else '|'
        print(''.join(l), c)

    return c


def parse(path):
    with open(path) as file:
        map = [[c for c in l.strip()] for l in file]

    for i, l in enumerate(map):
        for j, v in enumerate(l):
            if v == 'S':
                S = Point(i, j)
                break

    return S, map


def find_firsts(S, map):
    if 0 < S.x and map[S.x-1][S.y] in ['|', 'F', '7']:
        yield Point(S.x-1, S.y)
    if S.x < len(map)-1 and map[S.x+1][S.y] in ['|', 'L', 'J']:
        yield Point(S.x+1, S.y)
    if 0 < S.y and map[S.x][S.y-1] in ['-', 'L', 'F']:
        yield Point(S.x, S.y-1)
    if S.y < len(map[0])-1 and map[S.x][S.y+1] in ['-', '7', 'J']:
        yield Point(S.x, S.y+1)


def next_point(track, map):
    c = track[-1]
    p = track[-2]
    if map[c.x][c.y] == "|":
        x = c.x+1 if p.x < c.x else c.x - 1
        y = c.y
    elif map[c.x][c.y] == "-":
        x = c.x
        y = c.y+1 if p.y < c.y else c.y - 1
    elif map[c.x][c.y] == "L":
        x = c.x if p.x != c.x else c.x - 1
        y = c.y if p.y != c.y else c.y + 1
    elif map[c.x][c.y] == "J":
        x = c.x if p.x != c.x else c.x - 1
        y = c.y if p.y != c.y else c.y - 1
    elif map[c.x][c.y] == "7":
        x = c.x if p.x != c.x else c.x + 1
        y = c.y if p.y != c.y else c.y - 1
    elif map[c.x][c.y] == "F":
        x = c.x if p.x != c.x else c.x + 1
        y = c.y if p.y != c.y else c.y + 1
    return Point(x, y)


if __name__ == "__main__":
    #print(solve('sample'))
    print(solve('input'))
    #print(solve2('sample2'))
    #print(solve2('sample3'))
    #print(solve2('sample4'))
    #print(solve2('sample5'))
    print(solve2('input'))
