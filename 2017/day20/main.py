#!/usr/bin/env python

from __future__ import print_function
from __future__ import unicode_literals

import sys

from builtins import range
import re


def read_input(path):
    if not path:
        path = 'input.txt'
    with open(path) as f:
        lines = f.readlines()
    return lines


def distance(part):
    x, y, z = part[0]
    return abs(x) + abs(y) + abs(z)


def process_line(line):
    m = re.match(r'p=<\s?(-?\d+),\s?(-?\d+),\s?(-?\d+)>, v=<\s?(-?\d+),\s?(-?\d+),\s?(-?\d+)>, a=<\s?(-?\d+),\s?(-?\d+),\s?(-?\d+)>', line)
    return (int(m.group(1)), int(m.group(2)), int(m.group(3))), (int(m.group(4)), int(m.group(5)), int(m.group(6))), (int(m.group(7)), int(m.group(8)), int(m.group(9)))


def move(part):
    p, v, a = part
    nv = (v[0] + a[0], v[1] + a[1], v[2] + a[2])
    return (p[0] + nv[0], p[1] + nv[1], p[2] + nv[2]), nv, a


def p1(ps):
    i = 0
    last = None
    while i < 200:
        ps = list(map(move, ps))
        ds = list(map(distance, ps))
        m = ds.index(min(ds))
        if not last or last != m:
            last, i = m, 0
        elif last == m:
            i += 1
    return last


def p2(ps):
    no_removal = 0
    while no_removal < 20:
        ps = list(map(move, ps))

        to_remove = set()
        for i in range(len(ps)):
            for j in range(i + 1, len(ps)):
                if ps[i][0] == ps[j][0]:
                    to_remove.add(ps[i])
                    to_remove.add(ps[j])

        for r in to_remove:
            ps.remove(r)
            no_removal = 0
        else:
            no_removal += 1

    return len(ps)


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else None
    lines = read_input(path)
    lines = list(map(process_line, lines))

    s1 = p1(lines[:])
    print('Part 1:', s1)

    s2 = p2(lines[:])
    print('Part 2:', s2)


if __name__ == "__main__":
    main()
