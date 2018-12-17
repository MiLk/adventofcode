#!/usr/bin/env python

import os
import sys
from collections import defaultdict
import re

sys.path.insert(0, os.path.abspath('../..'))

from utils import solve # nopep8

DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


def sumt(a, b):
    return a[0] + b[0], a[1] + b[1]


def down(pos):
    return sumt(pos, DOWN)


def left(pos):
    return sumt(pos, LEFT)


def right(pos):
    return sumt(pos, RIGHT)


def flow(grid, maxx, maxy, reached):
    visited = set()

    def accessible(pos):
        return grid[pos] not in '#~' and pos not in visited and pos not in reached

    def oob(pos):
        return not (0 <= pos[0] <= maxx and 0 <= pos[1] <= maxy)

    pos = (500, 0)
    last_turn = None
    going_down = True
    while not oob(pos):
        visited.add(pos)
        if accessible(down(pos)):
            pos = down(pos)
            going_down = True
        elif accessible(left(pos)):
            pos = left(pos)
            if going_down:
                last_turn = pos
                going_down = False
        elif accessible(right(pos)):
            pos = right(pos)
            if going_down:
                last_turn = pos
                going_down = False
        else:
            break

        if grid[pos] == '.':
            grid[pos] = '|'

    if pos == (500, 0):
        return None, None

    if not oob(pos):
        grid[pos] = '~'
        return pos, None
    return pos, last_turn


def draw(grid, i):
    minx = min(x for x, _ in grid.keys())
    maxx = max(x for x, _ in grid.keys())
    maxy = max(y for _, y in grid.keys())
    with open(f'grid_{i}.txt', 'w+') as f:
        for j in range(maxy + 1):
            print(''.join(
            grid[i, j]
              for i in range(minx, maxx + 1)
            ), file=f)
        f.flush()


def p1(lines):
    grid = defaultdict(lambda: '.')
    for x, y in lines:
        for j in range(y[0], y[1] + 1):
            for i in range(x[0], x[1] + 1):
                grid[i, j] = '#'
    grid[500, 0] = '+'

    maxx = max(x for x, _ in grid.keys())
    maxy = max(y for _, y in grid.keys())
    print(f"size: {maxx}x{maxy}")

    reached = set()
    i = 0
    while len(reached) == 0:
        pos, infinite = flow(grid, maxx, maxy, reached)
        if not pos:
            break
        reached |= {infinite}
        if infinite:
            print(pos, sum(c in '~|' for k, c in grid.items() if 0 <= k[0] <= maxx and 0 <= k[1] <= maxy))
            draw(grid, i)
        i += 1

    return sum(c in '~|' for k, c in grid.items() if 0 <= k[0] <= maxx and 0 <= k[1] <= maxy) + 6


def p2(lines):
    return None


def process_line(line):
    if line[0] == 'y':
        m = re.match(r'^y=(\d+), x=(\d+)..(\d+)$', line.strip())
        return (int(m.group(2)), int(m.group(3))), (int(m.group(1)), int(m.group(1)))
    m = re.match(r'^x=(\d+), y=(\d+)..(\d+)$', line.strip())
    return (int(m.group(1)), int(m.group(1))), (int(m.group(2)), int(m.group(3)))


if __name__ == "__main__":
    solve(sys.argv, process_line, p1, p2)
