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
    if line[0] == 's':
        return line[0], int(line[1:])
    elif line[0] == 'x':
        a, b = line[1:].split('/')
        return line[0], (int(a), int(b))
    elif line[0] == 'p':
        return line[0], line[1:].split('/')


def p1(state, lines):
    for (k, v) in lines:
        if k == 's':
            state = state[-v:] + state[:-v]
        elif k == 'x':
            a, b = v
            state[b], state[a] = state[a], state[b]
        elif k == 'p':
            a, b = v
            pa, pb = state.index(a), state.index(b)
            state[pb], state[pa] = state[pa], state[pb]
    return state


def p2(state, lines, itr=1000000000):
    seen = []
    for i in range(itr):
        if seen and tuple(state) == seen[0]:
            return seen[itr % i]
        seen.append(tuple(state))

        for (k, v) in lines:
            if k == 's':
                state = state[-v:] + state[:-v]
            elif k == 'x':
                a, b = v
                state[b], state[a] = state[a], state[b]
            elif k == 'p':
                a, b = v
                pa, pb = state.index(a), state.index(b)
                state[pb], state[pa] = state[pa], state[pb]
    return state


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else None
    lines = read_input(path)[0].strip().split(',')
    lines = map(process_line, lines)

    state = [chr(ord('a') + i) for i in range(16)]
    s1 = p1(state[:], lines)
    print('Part 1:', ''.join(s1))

    s2 = p2(state, lines)
    print('Part 2:', ''.join(s2))


if __name__ == "__main__":
    main()
