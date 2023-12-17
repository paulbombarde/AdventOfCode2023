from functools import reduce
from operator import mul


def solve(races):
    return reduce(mul, (nb_wins(t,d) for t,d in races))


def nb_wins(race_time, race_dist):
    return sum(wins(race_time, race_dist, press_time) for press_time in range(race_time))


def wins(race_time, race_dist, press_time):
    return 1 if race_dist < press_time * (race_time - press_time) else 0


if __name__ == '__main__':
    sample = [(7, 9), (15, 40), (30, 200)]
    input = [(45, 295), (98, 1734), (83, 1278), (73, 1210)]
    print(solve(sample))
    print(solve(input))

    sample2 = (71530, 940200)
    input2 = (45988373, 295173412781210)
    print(nb_wins(sample2[0], sample2[1]))
    print(nb_wins(input2[0], input2[1]))
