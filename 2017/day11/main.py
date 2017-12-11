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


scores = {
    'n': (0, 2),
    'ne': (1, 1),
    'se': (1, -1),
    's': (0, -2),
    'sw': (-1, -1),
    'nw': (-1, 1)
}


def distance(pos):
    return (abs(pos[0]) + abs(pos[1])) / 2


def p1(moves):
    pos = (0, 0)
    furthest = 0

    for m in moves:
        offset = scores[m]
        pos = (pos[0] + offset[0], pos[1] + offset[1])
        d = distance(pos)
        if d > furthest:
            furthest = d

    return d, furthest


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else None
    lines = read_input(path)[0].strip().split(',')

    s1, s2 = p1(lines)
    print('Part 1:', s1)
    print('Part 2:', s2)


if __name__ == "__main__":
    main()
