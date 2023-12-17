def solve(sources, maps):
    for map in maps:
        sources = convert_sources(sources, map)
    return min(sources)


def solve2(sources, maps):
    sources = sorted([s for s in group_sources(sources)], key=lambda x:x[0])
    #print("sources", sources, "\n")
    for m in maps:
        #print("map", m)
        sources = sorted([s for s in convert_sources2(sources,m)])
        #print("sources", sources, "\n")
    return min(sources, key=lambda x:x[0])[0]


def parse(path):
    with open(path) as file:
        lines = (l.strip() for l in iter(file))
        sources = read_seeds(lines)
        maps = [m for m in read_maps(lines)]
    return sources, maps


def read_seeds(lines):
    _, seeds = next(lines).split(": ")
    next(lines)  # white line
    return [int(s) for s in seeds.split(" ")]


def read_maps(lines):
    while True:
        try:
            yield read_map(lines)
        except StopIteration:
            return


def read_map(lines):
    header = next(lines)
    return sorted(read_map_gen(lines), key=lambda x: x[0])


def read_map_gen(lines):
    line = next(lines)
    try:
        while len(line):
            dest, src, nb = (int(v) for v in line.split(" "))
            yield src, src+nb, dest-src # start, stop, delta
            line = next(lines)
    except StopIteration:
        pass


def convert_sources(sources, map):
    return [convert_source(s, map) for s in sources]


def convert_source(source, map):
    for start, stop, delta in map:
        if start <= source < stop:
            return source + delta
    return source


def convert_sources2(sources, map):
    for s,n in sources:
        yield from convert_source2(s, n, map)


def convert_source2(source_start, source_stop, map):
    #print("source", source_start, source_stop)
    for map_start, map_stop, delta in map:
        if source_start < map_start <= source_stop:
            yield source_start, map_start
            source_start = map_start
            #print("ici source", source_start, source_stop)
            if source_stop <= source_start:
                return

        if map_start <= source_start < map_stop:
            stop = min(source_stop, map_stop)
            yield source_start + delta, stop + delta
            source_start = stop
            #print("la source", source_start, source_stop)
            if source_stop <= source_start:
                return

    #print("fin source", source_start, source_stop)
    if not source_stop <= source_start:
        yield source_start, source_stop


def group_sources(sources):
    i = iter(sources)
    for s,n in zip(i, i):
        yield s, s+n # start, stop


if __name__ == '__main__':
    sources, maps = parse("/Users/logi/Repositories/AdventOfCode2023/Day5/input")
    print(solve(sources, maps))
    print(solve2(sources, maps))
