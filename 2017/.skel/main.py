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


def p1(line):
    return line


def p2(line):
    return line


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else None
    lines = read_input(path)
    lines = map(process_line, lines)

    s1 = map(p1, lines)
    print('Part 1:', s1)

    s2 = map(p2, lines)
    print('Part 2:', s2)


if __name__ == "__main__":
    main()
