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
    [reg, op, v, _, cr, cop, cv] = line.strip().split(' ')
    return reg, op, int(v), (cr, cop, int(cv))


def compare(op, a, b):
    if op == '>':
        return a > b
    elif op == '>=':
        return a >= b
    elif op == '==':
        return a == b
    elif op == '<=':
        return a <= b
    elif op == '<':
        return a < b
    elif op == '!=':
        return a != b
    else:
        raise RuntimeError('Unknown operator', op)


def solve(ops):
    rs = dict()
    m = 0
    for (r, op, v, (cr, cop, cv)) in ops:
        crv = rs.get(cr, 0)
        if compare(cop, crv, cv):
            rv = rs.get(r, 0)
            if op == 'inc':
                rs[r] = rv + v
            elif op == 'dec':
                rs[r] = rv - v
            else:
                raise RuntimeError('Unknown instruction', op)
        m = max(m, max(rs.values()))
    return max(rs.values()), m


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else None
    lines = read_input(path)
    lines = map(process_line, lines)
    s1, s2 = solve(lines)
    print('Part 1:', s1)
    print('Part 2:', s2)


if __name__ == "__main__":
    main()
