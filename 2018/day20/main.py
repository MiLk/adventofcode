#!/usr/bin/env python

import os
import sys
from collections import defaultdict
from queue import Queue

sys.path.insert(0, os.path.abspath('../..'))

from utils import solve, read_input  # nopep8


MOVES = {
    'N': (0, -1),
    'E': (1, 0),
    'S': (0, 1),
    'W': (-1, 0),
}


def move(a, m):
    b = MOVES[m]
    return a[0] + b[0], a[1] + b[1]


def build_options(line, i):
    opts = []
    d = 0
    v = ''
    while d > 0 or line[i] != ')':
        if line[i] == '|' and d == 0:
            opts.append(v)
            v = ''
        else:
            if line[i] == '(':
                d += 1
            elif line[i] == ')':
                d -= 1
            v += line[i]
        i += 1
    opts.append(v)

    return opts, i


def navigate(p, line, seen, doors):
    if (p, line) in seen:
        return seen, doors
    seen.add((p, line))

    i = 0
    while 0 <= i < len(line):
        if line[i] == '$':
            return seen, doors

        if line[i] == '^':
            i += 1
            continue

        # consume the string until next branch
        if line[i] in MOVES.keys():
            n = move(p, line[i])
            doors[p].add(n)
            doors[n].add(p)
            p = n
            i += 1
            continue

        if line[i] == '(':
            # build the options for the next block for one layer only
            opts, end = build_options(line, i + 1)
            # navigate all the options
            for opt in opts:
                seen, doors = navigate(p, opt + line[end + 1:], seen, doors)
            return seen, doors


def p1(lines):
    global distances

    start = (0, 0)
    _, doors = navigate(start, lines[0].strip(), set(), defaultdict(set))

    distances = {start: 0}
    q = Queue()
    q.put(start)
    while not q.empty():
        src = q.get()
        for dst in doors[src]:
            if dst not in distances:
                distances[dst] = distances[src] + 1
                q.put(dst)

    return max(distances.values())


def p2(_):
    global distances
    return len([k for k in distances if distances[k] >= 1000])


if __name__ == "__main__":
    solve(read_input(), lambda x: x, p1, p2)
