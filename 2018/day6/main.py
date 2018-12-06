#!/usr/bin/env python

import itertools
import os
import sys
from collections import Counter

sys.path.insert(0, os.path.abspath('../..'))

from utils import solve, str_line  # nopep8


def process_line(line):
    l = str_line(line).split(',')
    return int(l[0]), int(l[1].strip())


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def gen_grid(lines, size, offset=0):
    grid = dict()
    for i in range(-offset, size + offset):
        for j in range(- offset, size + offset):
            mC = '.'
            mV = 10000
            tie = False
            for l in lines:
                d = dist((i, j), l)
                if d < mV:
                    mV = d
                    mC = l
                    tie = False
                elif d == mV:
                    tie = True
            grid[(i, j)] = mC if not tie else '.'
    return grid


def p1(lines):
    boundary = max(max(i, j) for i, j in lines)
    fg = gen_grid(lines, boundary, 10)
    c = Counter(
        v for k, v in fg.items()
        if 0 <= k[0] <= boundary and 0 <= k[1] <= boundary
    )
    c2 = Counter(fg.values())
    d = {k: v for k, v in c.most_common()}
    d2 = {k: v for k, v in c2.most_common()}
    return max(v for k, v in d.items() if v == d2[k])


def p2(lines):
    boundary = max(max(i, j) for i, j in lines)
    grid = {
        (i, j): sum(dist((i, j), l) for l in lines)
        for i, j in itertools.product(range(0, boundary), range(0, boundary))
    }
    return sum(v < 10000 for v in grid.values())


if __name__ == "__main__":
    import time

    t1 = time.time()
    solve(sys.argv, process_line, p1, p2)
    t2 = time.time()
    print(t2 - t1)
