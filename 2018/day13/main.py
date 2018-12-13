#!/usr/bin/env python

import itertools
import os
import sys
from collections import defaultdict

sys.path.insert(0, os.path.abspath('../..'))

from utils import read_input  # nopep8

direction = {
    '^': (0, -1),
    '>': (1, 0),
    'v': (0, 1),
    '<': (-1, 0)
}

ltrun = {
    (0, -1): '<',
    (1, 0): '^',
    (0, 1): '>',
    (-1, 0): 'v'
}

rtrun = {
    (0, -1): '>',
    (1, 0): 'v',
    (0, 1): '<',
    (-1, 0): '^'
}


choices = ['<', '^', '>']


def turn(d, choice):
    if choice == 1:
        return d
    if choice == 0:
        return direction[ltrun[d]]
    if choice == 2:
        return direction[rtrun[d]]


def get_next_direction(track, d, choice):
    if track in ['|', '-', '^', 'v', '>', '<']:
        return d, choice
    if track == '/':
        if d == direction['^']:
            return direction['>'], choice
        if d == direction['>']:
            return direction['^'], choice
        if d == direction['v']:
            return direction['<'], choice
        if d == direction['<']:
            return direction['v'], choice
    if track == '\\':
        if d == direction['^']:
            return direction['<'], choice
        if d == direction['<']:
            return direction['^'], choice
        if d == direction['v']:
            return direction['>'], choice
        if d == direction['>']:
            return direction['v'], choice
    if track == '+':
        return turn(d, choice), (choice + 1) % len(choices)


def find_crash(x, y, carts):
    for c in carts:
        if x == c[0] and y == c[1]:
            return c
    return None


def tick(lines, carts, p1=False):
    carts = sorted(carts,key=lambda c: (c[1], c[0]))
    new_carts = []
    crashes = set()
    for i in range(len(carts)):
        x, y, d, choice = carts[i]
        if (x, y) in crashes:
            continue
        nx, ny = x + d[0], y + d[1]
        crash = find_crash(nx, ny, new_carts + carts[i+1:])
        if crash:
            if p1:
                return [f'{crash[0]},{crash[1]}']
            print('Crash', crash[0], crash[1])
            crashes.add((crash[0], crash[1]))
            continue
        nd = get_next_direction(lines[ny][nx], d, choice)
        new_carts.append((nx, ny, nd[0], nd[1]))

    return [
        c for c in new_carts
        if (c[0], c[1]) not in crashes
    ]


def get_carts(lines):
    return [
        (i, j, direction[lines[j][i]], 0)
        for j in range(len(lines))
        for i in range(len(lines[j]))
        if lines[j][i] in ['^', 'v', '<', '>']
    ]


def p1(lines):
    carts = get_carts(lines)
    for i in range(1000):
        carts = tick(lines, carts, True)
        if len(carts) == 1:
            return carts[0]


def p2(lines):
    carts = get_carts(lines)
    for i in range(50_000):
        if len(carts) == 1:
            return f"{carts[0][0],carts[0][1]}"
        carts = tick(lines, carts)


def solve(argv, p1, p2):
    lines = argv if len(argv) > 1 else read_input()

    s1 = p1(lines)
    print('Part 1:', s1)

    s2 = p2(lines)
    print('Part 2:', s2)


if __name__ == "__main__":
    solve(sys.argv, p1, p2)
