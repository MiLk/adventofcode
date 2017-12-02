#!/usr/bin/env python

from __future__ import print_function
from __future__ import unicode_literals

import sys


def readinput(path):
    if not path:
        path = 'input.txt'
    with open(path) as f:
        lines = f.readlines()
    return lines


def process_line(line):
    return [int(i) for i in line.split('\t')]


def p1(n):
    return max(n) - min(n)


def p2(n):
    for i in xrange(0, len(n)):
        for j in xrange(i + 1, len(n)):
            if i == j:
                continue
            a, b = max([n[i], n[j]]), min([n[i], n[j]])
            if a % b == 0:
                return a / b


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else None
    lines = map(process_line, readinput(path))
    print('Part 1: %d' % sum(map(p1, lines)))
    print('Part 2: %d' % sum(map(p2, lines)))


if __name__ == "__main__":
    main()
