#!/usr/bin/env python

import itertools
import os
import sys
from collections import defaultdict

sys.path.insert(0, os.path.abspath('../..'))

from utils import solve, int_line, int_list_line, str_list_line  # nopep8


def claim(line):
    sp = line.strip().split()
    n = int(sp[0][1:])
    l, t = sp[2].strip(':').split(',')
    w, h = sp[3].split('x')
    return n, int(l), int(t), int(w), int(h)


def p1m(claims):
    fabric = defaultdict(int)
    for _, l, t, w, h in claims:
        for i, j in itertools.product(range(l, l+w), range(t, t+h)):
            fabric[(i, j)] += 1
    return sum(1 if v >= 2 else 0 for v in fabric.values())


def p1(claims):
    claimed = set()
    overclaimed = set()
    for _, l, t, w, h in claims:
        for i, j in itertools.product(range(l, l+w), range(t, t+h)):
            if (i, j) in claimed:
                overclaimed.add((i, j))
            claimed.add((i, j))
    return len(overclaimed)


def p2(claims):
    claimed = dict()
    overclaimed = set()
    ids = set()
    for n, l, t, w, h in claims:
        ids.add(n)
        for i, j in itertools.product(range(l, l+w), range(t, t+h)):
            if len(claimed.get((i, j), set())) > 0:
                overclaimed = overclaimed | {n} | claimed[(i, j)]
            claimed[(i, j)] = claimed.get((i, j), set()) | {n}
    return ids - overclaimed


if __name__ == "__main__":
    solve(sys.argv, claim, p1, p2)
