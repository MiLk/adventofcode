#!/usr/bin/env python

from __future__ import print_function
from __future__ import unicode_literals

import sys

from builtins import range


def read_input(path):
    if not path:
        path = 'input.txt'
    with open(path) as f:
        lines = f.readlines()
    return lines


def process_line(line):
    p = line.strip().split(' ')
    return int(p[0]), [int(pp.strip(',')) for pp in p[2:]]


def p1(programs, start=0):
    seen = set()

    def search(p):
        if p in seen:
            return 0
        seen.add(p)
        ps = programs[p]
        return 1 + sum([search(c) for c in ps])

    return search(start), seen


def p2(programs):
    seen = set()
    groups = 0

    for i in programs.keys():
        if i in seen:
            continue
        _, s = p1(programs, i)
        seen.update(s)
        groups += 1

    return groups


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else None
    lines = read_input(path)
    programs = dict(map(process_line, lines))

    s1, _ = p1(programs)
    print('Part 1:', s1)

    s2 = p2(programs)
    print('Part 2:', s2)


if __name__ == "__main__":
    main()
