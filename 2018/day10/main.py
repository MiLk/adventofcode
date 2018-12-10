#!/usr/bin/env python

import itertools
import os
import sys
from collections import defaultdict

sys.path.insert(0, os.path.abspath('../..'))

from utils import solve, int_line, int_list_line, str_line, str_list_line  # nopep8


def process_line(line):
    p = line[10:24].split(',')
    v = line[36:42].split(',')
    return (int(p[0].strip()), int(p[1].strip())), (int(v[0].strip()), int(v[1].strip()))


def position_at(line, n):
    p, v = line
    return p[0] + n * v[0], p[1] + n * v[1]


def draw(lines, n=0, dry=True):
    grid = defaultdict(lambda: ' ')
    for l in lines:
        np = position_at(l, n)
        grid[np] = '#'
    minx = min(p[0] for p in grid.keys())
    maxx = max(p[0] for p in grid.keys())
    miny = min(p[1] for p in grid.keys())
    maxy = max(p[1] for p in grid.keys())
    if not dry:
        for j in range(miny, maxy +1):
            print(''.join(grid[(i, j)] for i in range(minx, maxx + 1)))
    return minx, maxx, miny, maxy


def p1(lines):
    tx, ty = p2(lines)
    draw(lines, tx, dry=False)
    if tx != ty:
        draw(lines, ty, dry=False)
    return None


def p2(lines):
    dx = dict()
    dy = dict()
    for i in range(9900, 10100):
        minx, maxx, miny, maxy = draw(lines, i)
        dx[i] = maxx - minx
        dy[i] = maxy - miny

    mx = min(dx.values())
    my = min(dy.values())
    tx = next(k for k,v in dx.items() if v == mx)
    ty = next(k for k,v in dy.items() if v == my)
    return tx, ty


if __name__ == "__main__":
    solve(sys.argv, process_line, p1, p2)
