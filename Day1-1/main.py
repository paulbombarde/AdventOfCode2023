# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def solve(path):
    with open(path) as file:
        print(sum((value(l) for l in file)))

def value(line):
    first = first_digit(line)
    last = first_digit(reversed(line))
    val = first+last
    return int(val)

def first_digit(line):
    for c in line:
        if c.isdigit():
            return c


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solve("/Users/logi/Repositories/AdventOfCode2023/Day1-1/input")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
