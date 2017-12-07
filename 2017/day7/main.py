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
    s = line.strip().split(' ', 3)
    name = s[0]
    weight = int(s[1].lstrip('(').rstrip(')'))
    children = s[3].split(', ') if len(s) > 3 else []
    return name, weight, children


def p1(ps):
    has_parent = set()
    for (_,_, children) in ps:
        for c in children:
            has_parent.add(c)
    for (name, _, _) in ps:
        if name not in has_parent:
            return name
    return None


def _weight(ps, disc):
    (w, children, _, _) = ps[disc]
    cw = [_weight(ps, c) for c in children]
    if len(set(cw)) > 2:
        print(disc, w, children, cw)
    t = w + sum(cw)
    ps[disc] = (w, children, t, cw)
    return t


def _print(ps, disc, diff=None):
    if len(set(ps[disc][3])) > 1:
        cw = ps[disc][3]
        for w in set(cw):
            if cw.count(w) == 1:
                return _print(ps, ps[disc][1][cw.index(w)], w - list(set(cw) - {w})[0])
    else:
        return ps[disc][0] - diff


def p2(lines, bottom):
    ps = dict()
    for (name, weight, children) in lines:
        ps[name] = (weight, children, 0, [])
    _weight(ps, bottom)
    return _print(ps, bottom)


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else None
    lines = read_input(path)
    lines = list(map(process_line, lines))

    s1 = p1(lines)
    print('Part 1:', s1)

    s2 = p2(lines, s1)
    print('Part 2:', s2)


if __name__ == "__main__":
    main()
