#!/usr/bin/env python

from __future__ import print_function
from __future__ import unicode_literals

import sys


def read_input(path):
    if not path:
        path = 'input.txt'
    with open(path) as f:
        lines = f.readlines()
    return lines


def process_line(line):
    return line.strip().split(' ')


def is_valid(words):
    return len(set(words)) == len(words)


def is_valid_2(words):
    return len(set([str(sorted(word)) for word in words])) == len(words)


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else None
    lines = read_input(path)
    lines = list(map(process_line, lines))

    s1 = list(filter(is_valid, lines))
    print('Part 1: %d' % len(s1))

    s2 = list(filter(is_valid_2, lines))
    print('Part 2: %d' % len(s2))


if __name__ == "__main__":
    main()
