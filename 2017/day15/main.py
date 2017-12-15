#!/usr/bin/env python

from __future__ import print_function
from __future__ import unicode_literals

import sys

from builtins import range
import re


def read_input(path):
    if not path:
        path = 'input.txt'
    with open(path) as f:
        lines = f.readlines()
    return lines


def process_line(line):
    m = re.match(r'Generator (\w) starts with (\d+)', line.strip())
    return m.groups()


def next_value(f, v):
    return (v * f) % 2147483647


def p1(t):
    (a, b) = t
    return next_value(16807, a), next_value(48271, b)


def p2(t):
    (a, b) = t
    na = next_value(16807, a)
    while na % 4 != 0:
        na = next_value(16807, na)
    nb = next_value(48271, b)
    while nb % 8 != 0:
        nb = next_value(48271, nb)
    return na, nb


def solve(gens, n, itr=40*1000*1000):
    (a, b) = gens
    c = 0
    for _ in range(itr):
        (a, b) = n((a, b))
        al = a & 0xffff
        bl = b & 0xffff
        if al == bl:
            c += 1

    return c


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else None
    lines = read_input(path)
    gens = tuple(int(l[1]) for l in map(process_line, lines))

    print('Part 1:', solve(gens, p1))
    print('Part 2:', solve(gens, p2, 5 * 1000 * 1000))


if __name__ == "__main__":
    main()
