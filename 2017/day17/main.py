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


def process_line(line):
    return [int(n) for n in line.strip().split('\t')]


def p1(steps, goal=2017, itr=2017):
    buf = [0]
    cur = 0
    for i in range(1, 1 + itr):
        cur = ((cur + steps) % i) + 1
        buf.insert(cur, i)

    return buf[buf.index(goal)+1]


def p2(steps, goal=0, itr=50000000):
    cur = 0
    after_goal = None
    for i in range(1, 1 + itr):
        cur = ((cur + steps) % i) + 1
        if cur == (goal + 1):
            after_goal = i

    return after_goal


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else None
    data = int(read_input(path)[0].strip())

    s1 = p1(data)
    print('Part 1:', s1)

    s2 = p2(data)
    print('Part 2:', s2)


if __name__ == "__main__":
    main()
