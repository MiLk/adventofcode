import itertools
import math

from utils import int_lines

parse_input = int_lines


def p1(lines):
    for n in sorted(lines):
        if (2020 - n) in lines:
            return n * (2020 - n)


def p2(lines):
    for c in itertools.combinations(lines, 3):
        if sum(c) == 2020:
            return math.prod(c)
