#!/usr/bin/env python

import os
import sys

sys.path.insert(0, os.path.abspath('../..'))

from utils import solve, str_line  # nopep8


def react(a, b):
    return abs(ord(a) - ord(b)) == 32


def full_react(line):
    i = 0
    while i < (len(line) - 1):
        if react(line[i], line[i+1]):
            line = line[:i] + line[i+2:]
            i = max(0, i - 1)
        else:
            i += 1
    return len(line)


def p1(lines):
    return full_react(lines[0])


def p2(lines):
    return min(
        full_react(lines[0].replace(chr(i), '').replace(chr(i + 32), ''))
        for i in range(ord('A'), ord('Z') + 1)
    )


if __name__ == "__main__":
    solve(sys.argv, str_line, p1, p2)
