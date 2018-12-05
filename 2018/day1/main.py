#!/usr/bin/env python

import itertools
import os
import sys

sys.path.insert(0, os.path.abspath('../..'))

from utils import solve, int_line, int_list_line  # nopep8


def p1(lines):
    return sum(lines)


def p2(lines):
    seen = set()
    f = 0
    for l in itertools.cycle(lines):
        seen.add(f)
        f += l
        if f in seen:
            return f


if __name__ == "__main__":
    solve(sys.argv, int_line, p1, p2)
