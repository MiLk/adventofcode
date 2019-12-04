from collections import Counter
from itertools import tee


def parse_input(lines):
    lower, upper = tuple(int(n) for n in lines[0].strip().split('-'))
    return tee(
        n
        for n in map(str, range(lower, upper + 1))
        if sorted(n) == list(n)
    )


def p1(numbers):
    return sum(
        any(x >= 2 for x in Counter(digits).values())
        for digits in numbers[0]
    )


def p2(numbers):
    return sum(
        any(x == 2 for x in Counter(digits).values())
        for digits in numbers[1]
    )
