#!/usr/bin/env python

import itertools
import os
import sys
from math import floor

sys.path.insert(0, os.path.abspath('../..'))

from utils import solve, int_line  # nopep8


def power_level(sn, x, y):
    rack_id = x + 10
    pl = rack_id * y
    pl += sn
    pl *= rack_id
    pl = floor(pl / 100)
    pl %= 10
    return pl - 5


def power_sum(grid, i, j, s=3):
    return sum(
        grid[(x, y)]
        for (x, y) in itertools.product(range(i, i + s), range(j, j + s))
    )


def gen_grid(sn):
    return {
        (i + 1, j + 1): power_level(sn, i + 1, j + 1)
        for (i, j) in itertools.product(range(300), range(300))
    }


def _solve(sn, sizes):
    grid = gen_grid(sn)

    best = (None, 0)
    for s in sizes:
        print("Size: %d" % s)
        for (i, j) in itertools.product(range(1, 300 - (s - 2)), range(1, 300 - (s - 2))):
            ps = power_sum(grid, i, j, s)
            if ps > best[1]:
                best = ("%dx%dx%d" % (s, i, j), ps)
                if s > 3:
                    print(best)
    return best


def p1(lines):
    return _solve(lines[0], [3])[0][2:]


def p2(lines):
    return _solve(lines[0], range(15))[0]


if __name__ == "__main__":
    assert power_level(8, 3, 5) == 4
    assert power_level(57, 122, 79) == -5
    assert power_level(39, 217, 196) == 0
    assert power_level(71, 101, 153) == 4
    solve(sys.argv, int_line, p1, p2)
