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


def p1dict(claims):
    fabric = defaultdict(int)
    for _, l, t, w, h in claims:
        for i, j in itertools.product(range(l, l+w), range(t, t+h)):
            fabric[(i, j)] += 1
    return sum(v >= 2 for v in fabric.values())


def p1set(claims):
    claimed = set()
    overclaimed = set()
    for _, l, t, w, h in claims:
        current = set(itertools.product(range(l, l+w), range(t, t+h)))
        overclaimed |= (current & claimed)
        claimed |= current
    return len(overclaimed)


def p2(claims):
    claimed = defaultdict(set)
    overclaimed = set()
    ids = set()
    for n, l, t, w, h in claims:
        ids.add(n)
        for i, j in itertools.product(range(l, l+w), range(t, t+h)):
            if len(claimed[(i, j)]) > 0:
                overclaimed |= {n} | claimed[(i, j)]
            claimed[(i, j)] |= {n}
    return ids - overclaimed


if __name__ == "__main__":
    solve(sys.argv, claim, p1set, p2)
