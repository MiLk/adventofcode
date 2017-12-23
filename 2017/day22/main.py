#!/usr/bin/env python

from __future__ import print_function
from __future__ import unicode_literals

import sys

from builtins import range


def read_input(path):
    if not path:
        path = 'input.txt'
    with open(path) as f:
        lines = f.readlines()
    return lines


def p1(m, s, itr):
    i = s // 2
    j = i
    d = (0, -1)

    b = 0

    for _ in range(itr):
        if m.get((i, j), '.') == '#':
            if d[0] == 0:
                d = (-d[1], 0)
            else:
                d = (0, d[0])
            m[(i, j)] = '.'
        else:
            if d[0] == 0:
                d = (d[1], 0)
            else:
                d = (0, - d[0])
            b += 1
            m[(i, j)] = '#'
        i += d[0]
        j += d[1]

    return b


def p2(m, s, itr):
    i = s // 2
    j = i
    d = (0, -1)

    b = 0

    for _ in range(itr):
        s = m.get((i, j), '.')
        if s == '.':
            d = (d[1], - d[0])
            m[(i, j)] = 'W'
        elif s == 'W':
            b += 1
            m[(i, j)] = '#'
        elif s == 'F':
            d = (-d[0], -d[1])
            m[(i, j)] = '.'
        elif s == '#':
            d = (- d[1], d[0])
            m[(i, j)] = 'F'

        i += d[0]
        j += d[1]

    return b


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else None
    lines = read_input(path)
    s = len(lines)
    m = {
        (i, j): c
        for j, line in enumerate(lines)
        for i, c in enumerate(line.strip())
    }

    s1 = p1(m.copy(), s, 10000)
    print('Part 1:', s1)

    s2 = p2(m.copy(), s, 10000000)
    print('Part 2:', s2)


if __name__ == "__main__":
    main()
