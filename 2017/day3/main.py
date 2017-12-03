#!/usr/bin/env python

from __future__ import print_function
from __future__ import unicode_literals

from builtins import range

import math
import sys


def read_input(path):
    if not path:
        path = 'input.txt'
    with open(path) as f:
        lines = f.readlines()
    return lines


def find_steps(n):
    """Return the number of steps to reach cell 1

    >>> find_steps(1)
    0
    >>> find_steps(12)
    3
    >>> find_steps(16)
    3
    >>> find_steps(18)
    3
    >>> find_steps(22)
    3
    >>> find_steps(23)
    2
    >>> find_steps(27)
    4
    >>> find_steps(33)
    4
    >>> find_steps(35)
    4
    >>> find_steps(39)
    4
    >>> find_steps(41)
    4
    >>> find_steps(1024)
    31
    >>> find_steps(289326)
    419
    >>> find_steps(347991)
    480
    """

    # find the size (columns/rows) of the smallest square which contains n
    size = math.ceil(math.sqrt(n))
    # find biggest number of the square
    m = size * size
    # used to calculate position of the cell with 1
    middle = size / 2
    # first cell bottom row
    bottom = m - size + 1

    if n >= bottom:
        middle_cell = math.floor(bottom + middle)
        return int(abs(n - middle_cell) + math.floor(middle))
    else:
        middle_cell = math.ceil(bottom - size + middle)
        return int(abs(n - middle_cell) + math.floor(middle))


def print_spiral(grid, n, m):
    for j in range(-m, m+1):
        print("\t".join(["{0:6}".format(grid[j][i]) for i in range(-n, n +1)]))
    print()


def gen_spiral(n):
    grid = {0: {0: 1}}
    i, j = 1, 0
    min_i, max_i, min_j, max_j = 0, 1, 0, 0
    last_move = 'R'
    while True:
        if j not in grid:
            grid[j] = {}
        s = sum([
            grid.get(j, {}).get(i - 1, 0),
            grid.get(j, {}).get(i + 1, 0),
            grid.get(j - 1, {}).get(i - 1, 0),
            grid.get(j - 1, {}).get(i, 0),
            grid.get(j - 1, {}).get(i + 1, 0),
            grid.get(j + 1, {}).get(i - 1, 0),
            grid.get(j + 1, {}).get(i, 0),
            grid.get(j + 1, {}).get(i + 1, 0),
        ])
        grid[j][i] = s
        if i > 0 and i == j:
            print_spiral(grid, j, i)
        if s >= n:
            break
        if last_move == 'R':
            if i == max_i:
                j -= 1
                min_j -= 1
                last_move = 'U'
            else:
                i += 1
        elif last_move == 'U':
            if j == min_j:
                i -= 1
                min_i -= 1
                last_move = 'L'
            else:
                j -= 1
        elif last_move == 'L':
            if i == min_i:
                j += 1
                max_j += 1
                last_move = 'D'
            else:
                i -= 1
        elif last_move == 'D':
            if j == max_j:
                i += 1
                max_i += 1
                last_move = 'R'
            else:
                j += 1

    print('Part 2:', s)


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else None
    _input = int(read_input(path)[0].strip())

    print("Part 1: %d" % find_steps(_input))
    gen_spiral(_input)


if __name__ == "__main__":
    main()
