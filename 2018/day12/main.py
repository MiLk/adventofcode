#!/usr/bin/env python

import itertools
import os
import sys
from collections import deque

sys.path.insert(0, os.path.abspath('../..'))

from utils import read_input  # nopep8


def process_init(line):
    return line.split(':')[1].strip()


def process_line(line):
    return line[:5], line[9]


def gen(state, idx, transitions):
    while not state.startswith('....'):
        idx -= 1
        state = '.' + state
    while not state.endswith('....'):
        state = state + '.'

    new_state = ''
    for i in range(2, len(state) - 2):
        new_state += transitions.get(state[i-2:i+3], '.')
    return new_state, idx + 2


def p1(state, transitions):
    print('0: 0 -', state)
    idx = 0
    for i in range(20):
        state, idx = gen(state, idx, transitions)
        print('%s: %d - %s' % (i + 1, idx, state))
    return sum(
        i + idx
        for i in range(len(state))
        if state[i] == '#'
    )


def p2(state, transitions):
    ngen = 50000000000
    idx = 0
    ratio = deque([], maxlen=5)
    for i in range(ngen):
        state, idx = gen(state, idx, transitions)
        s = sum(
            i + idx
            for i in range(len(state))
            if state[i] == '#'
        )
        #print('%s: %d - %d' % (i + 1, s, s / (i + 1)))
        ratio.append(s / (i + 1))
        if len(ratio) > 1 and len(set(ratio)) == 1:
            return int(ratio[0]) * ngen


def solve(argv, p1, p2):
    text_input = argv if len(argv) > 1 else read_input()
    state = process_init(text_input[0])
    lines = { k: v for (k, v) in map(process_line, text_input[2:]) }

    s1 = p1(state, lines)
    print('Part 1:', s1)

    s2 = p2(state, lines)
    print('Part 2:', s2)


if __name__ == "__main__":
    solve(sys.argv, p1, p2)
