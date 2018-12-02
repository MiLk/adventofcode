#!/usr/bin/env python

import os
import sys

sys.path.insert(0, os.path.abspath('../..'))

from utils import solve, str_line # nopep8


def count_letter(s, l):
    n = 0
    for c in s:
        if c == l:
            n = n +1
    return n


def has_same_letter(s, expected):
    for l in s:
        n = count_letter(s, l)
        if n == expected:
            return True
    return False


def p1(lines):
    c2 = 0
    c3 = 0
    for id in lines:
        if has_same_letter(id, 2):
            c2 = c2 + 1
        if has_same_letter(id, 3):
            c3 = c3 + 1
    return c2 * c3


def common(s1, s2):
    return ''.join([
        s1[i]
        for i in range(max(len(s1), len(s2)))
        if s1[i] == s2[i]
    ])


def p2(lines):
    import itertools
    from jellyfish import levenshtein_distance
    for (l1, l2) in itertools.product(lines, repeat=2):
        d = levenshtein_distance(l1, l2)
        if d == 1:
            return common(l1, l2)


if __name__ == "__main__":
    solve(sys.argv, str_line, p1, p2)
