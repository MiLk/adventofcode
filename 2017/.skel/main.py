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
    return line


def main():
    lines = readinput(sys.argv[1])
    lines = map(process_line, lines)

    print('Part 1: %d' % 0)

    print('Part 2: %d' % 0)


if __name__ == "__main__":
    main()
