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
    return int(line.strip())


def p1(instructions):
    i = 0
    steps = 0
    while i < len(instructions):
        off = instructions[i]
        instructions[i] += 1
        i += off
        steps += 1
    return steps


def p2(instructions):
    i = 0
    steps = 0
    while i < len(instructions):
        off = instructions[i]
        if off >= 3:
            instructions[i] -= 1
        else:
            instructions[i] += 1
        i += off
        steps += 1
    return steps


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else None
    lines = read_input(path)
    instructions = map(process_line, lines)

    print('Part 1:', p1(instructions[:]))
    print('Part 2:', p2(instructions[:]))


if __name__ == "__main__":
    main()
