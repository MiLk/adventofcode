#!/usr/bin/env python

import itertools
import os
import sys

sys.path.insert(0, os.path.abspath('../..'))

from utils import solve, str_line  # nopep8

SIZE = 50


def get_grid(lines):
    return {
        (i, j): lines[j][i]
        for i, j in itertools.product(range(SIZE), range(SIZE))
    }


def adjacent(x, y):
    return (
        (x + i, y + j)
        for i, j in itertools.product([-1, 0, 1], repeat=2)
        if (i != 0 or j != 0) and 0 <= x + i < SIZE and 0 <= y + j < SIZE
    )


def convert(grid, pos):
    c = grid[pos]
    adj = [grid[p] for p in adjacent(*pos)]
    if c == '.':
        return '|' if sum(c == '|' for c in adj) >= 3 else c
    elif c == '|':
        return '#' if sum(c == '#' for c in adj) >= 3 else c
    else:
        return c if '#' in adj and '|' in adj else '.'


def convert_all(grid):
    return {
        pos: convert(grid, pos)
        for pos in grid.keys()
    }


def draw(grid):
    for j in range(SIZE):
        print(''.join(
            grid[i, j]
            for i in range(SIZE)
        ))


def p1(lines):
    grid = get_grid(lines)
    for i in range(0, 10):
        grid = convert_all(grid)
    w = sum(c == '|' for c in grid.values())
    l = sum(c == '#' for c in grid.values())
    return w * l


def p2(lines):
    grid = get_grid(lines)
    values = []
    for i in range(0, 650):
        grid = convert_all(grid)
        w = sum(c == '|' for c in grid.values())
        l = sum(c == '#' for c in grid.values())
        v = w * l
        values.append(v)
        if values[-28:] == values[-56:-28]:
            a = values.index(v)
            offset = (1_000_000_000 - a) % (i - a)
            return values[a + offset - 1]


if __name__ == "__main__":
    solve(sys.argv, str_line, p1, p2)
