#!/usr/bin/env python

from __future__ import print_function
from __future__ import unicode_literals

import sys

from builtins import range
import collections


def read_input(path):
    if not path:
        path = 'input.txt'
    with open(path) as f:
        lines = f.readlines()
    return lines


def process_line(line):
    return tuple(int(n) for n in line.strip().split('/'))


def solve(by_port, available, bridge):
    start = bridge[0]
    for c in by_port[start] & available:
        last = c[0] if c[1] == start else c[1]
        for b in solve(by_port, available - frozenset([c]), (last, bridge[1] + c[0] + c[1], bridge[2] + 1)):
            yield b
    else:
        yield bridge


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else None
    lines = read_input(path)
    components = frozenset(map(process_line, lines))

    by_port = collections.defaultdict(set)
    for c in components:
        by_port[c[0]].add(c)
        by_port[c[1]].add(c)

    bridges = list(solve(by_port, components, (0, 0, 0)))
    s1 = max(bridges, key=lambda b: b[1])
    print('Part 1:', s1[1])

    s2 = max(bridges, key=lambda b: (b[2], b[1]))
    print('Part 2:', s2[1])


if __name__ == "__main__":
    main()
