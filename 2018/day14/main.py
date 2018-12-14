#!/usr/bin/env python

import itertools
import os
import sys
from collections import defaultdict

sys.path.insert(0, os.path.abspath('../..'))

from utils import solve, int_line, int_list_line, str_line, str_list_line  # nopep8


def p1(lines):
    n = lines[0]
    scores = '37'
    e = 0, 1
    for i in range(1, n + 10):
        ra, rb = int(scores[e[0]]), int(scores[e[1]])
        scores += f"{ra + rb}"
        e = ((e[0] + 1 + ra) % len(scores), (e[1] + 1 + rb) % len(scores))

    return scores[n:n+10]


def p2(lines):
    n = [int(d) for d in str(lines[0])]
    scores = [3, 7]
    e = 0, 1

    while scores[-len(n):] != n and scores[-len(n)-1:-1] != n:
        ra, rb = scores[e[0]], scores[e[1]]
        nr = ra + rb
        scores.extend(divmod(nr, 10) if nr >= 10 else (nr,))
        e = ((e[0] + 1 + ra) % len(scores), (e[1] + 1 + rb) % len(scores))

    return len(scores) - len(n) - (0 if scores[-len(n):] == n else 1)


if __name__ == "__main__":
    solve([79303], int_line, p1, p2)
