#!/usr/bin/env python

import itertools
import math
import os
import re
import sys
from collections import defaultdict, Counter
from z3 import *

sys.path.insert(0, os.path.abspath('../..'))

from utils import solve # nopep8


def dist(a, b):
    a1, a2, a3 = a
    b1, b2, b3 = b
    return abs(a1 - b1) + abs(a2 - b2) + abs(a3 - b3)


def in_range(src, n):
    return dist(src[0], n) <= src[1]


def p1(lines):
    strongest = max(lines, key=lambda l: l[1])
    return sum(
        in_range(strongest, l[0])
        for l in lines
    )


def p2counter(lines):
    inrange = defaultdict(int)
    i = 0
    for n in lines:
        p, r = n
        print(i)
        for x, y, z in itertools.product(
            range(p[0] - r, p[0] + r + 1),
            range(p[1] - r, p[1] + r + 1),
            range(p[2] - r, p[2] + r + 1),
        ):
            inrange[x, y, z] += 1
        i += 1

    c = Counter(inrange)
    return c.most_common()


def p2loop(lines):
    lowest = min(lines, key=lambda l: l[1])
    step = math.floor(lowest[1] / 16)

    minx = min(l[0][0] for l in lines)
    maxx = max(l[0][0] for l in lines)
    miny = min(l[0][1] for l in lines)
    maxy = max(l[0][1] for l in lines)
    minz = min(l[0][2] for l in lines)
    maxz = max(l[0][2] for l in lines)

    inrange = defaultdict(int)
    for i in range(minx, maxx + 1, step):
        for j in range(miny, maxy + 1, step):
            for k in range(minz, maxz + 1, step):
                inrange[i, j, k] = sum(
                    in_range(l, (i, j, k))
                    for l in lines
                )

    c = Counter(inrange)
    return c.most_common(5)


def p2discover(lines):
    inrange = defaultdict(int)
    for n in lines:
        inrange[n[0]] = sum(
            in_range(l, n[0])
            for l in lines
        )

    c = Counter(inrange)
    return c.most_common(5)


def p2sat(lines):
    nanobots = [n for n in lines]

    def zabs(x):
        return If(x >= 0, x, -x)

    (x, y, z) = (Int('x'), Int('y'), Int('z'))
    in_ranges = [
        Int('in_range_' + str(i)) for i in range(len(nanobots))
    ]
    range_count = Int('sum')
    o = Optimize()
    for i in range(len(nanobots)):
        (nx, ny, nz), nrng = nanobots[i]
        o.add(in_ranges[i] == If(zabs(x - nx) + zabs(y - ny) + zabs(z - nz) <= nrng, 1, 0))
    o.add(range_count == sum(in_ranges))
    dist_from_zero = Int('dist')
    o.add(dist_from_zero == zabs(x) + zabs(y) + zabs(z))
    o.maximize(range_count)
    h2 = o.minimize(dist_from_zero)
    o.check()
    return o.lower(h2), o.upper(h2)


def process_line(line):
    m = re.match(r'pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)', line.strip())
    g = m.groups()
    return (int(g[0]), int(g[1]), int(g[2])), int(g[3])


if __name__ == "__main__":
    solve(sys.argv, process_line, p1, p2sat)
