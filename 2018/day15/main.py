#!/usr/bin/env python

import os
import sys
from collections import defaultdict, deque


sys.path.insert(0, os.path.abspath('../..'))

from utils import solve, str_line  # nopep8


def get_grid(lines, eap):
    walls = {
        (i, j)
        for j in range(len(lines))
        for i in range(len(lines[0]))
        if lines[j][i] == '#'
    }
    units = [
        Unit(i, j, lines[j][i], 3 if lines[j][i] == 'G' else eap)
        for j in range(len(lines))
        for i in range(len(lines[0]))
        if lines[j][i] in ['G', 'E']
    ]
    return walls, units


def occupied_cells(units):
    return {
        u.pos
        for u in units
        if u.hp > 0
    }


def bfs(s, occ, goals):
    visited = defaultdict(bool)
    visited[s] = True

    check = deque([[s]])
    while len(check):
        path = check.popleft()
        c = path[-1]
        if c in goals:
            return path
        for dy, dx in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            x, y = c[0] + dx, c[1] + dy
            if (x, y) not in occ and not visited[x, y]:
                visited[x, y] = True
                check.append(path+[(x, y)])
    return []


class Unit:
    pos = None
    type = None
    ap = 0
    hp = 200

    def __init__(self, x, y, type, ap):
        self.pos = (x, y)
        self.type = type
        self.ap = ap

    def __str__(self):
        return f"{self.type}({self.hp}):{self.pos[0]}x{self.pos[1]}"

    def __repr__(self):
        return str(self)

    def find_targets(self, units):
        return list(filter(lambda u: u.hp > 0 and u.type != self.type, units))

    def adjacents(self, units=None):
        if not units:
            return [
                (self.pos[0], self.pos[1] - 1),
                (self.pos[0] + 1, self.pos[1]),
                (self.pos[0], self.pos[1] + 1),
                (self.pos[0] - 1, self.pos[1]),
            ]

        return sorted([
            u
            for u in units
            if u.hp > 0 and (abs(u.pos[0] - self.pos[0]) + abs(u.pos[1] - self.pos[1])) == 1
        ], key=lambda u: (u.hp, u.pos[1], u.pos[0]))

    def hit(self, target):
        # print(f"{self} hits {target}")
        target.hp -= self.ap
        if target.hp <= 0 and target.type == 'E':
            return True

    def find_path(self, goals, occ):
        b = bfs(self.pos, occ, goals)
        if not b:
            return None, None
        return b[1], len(b) - 1

    def move(self, pos):
        if not pos:
            return
        # print(f"{self} move to {pos}")
        self.pos = pos


def draw(walls, units, cu=None):
    grid = defaultdict(lambda: '.')
    for w in walls:
        grid[w] = '#'
    for u in units:
        if u.hp > 0:
            grid[u.pos] = u.type

    if cu:
        grid[cu.pos] = cu.type.lower()

    my = max(y for (_, y) in grid.keys())
    mx = max(x for (x, _) in grid.keys())
    for y in range(my+1):
        print(''.join(grid[(x, y)] for x in range(mx + 1)))


def is_valid(p):
    return p[0] is not None and p[1] is not None


def _solve(lines, eap=3):
    walls, units = get_grid(lines, eap)
    rn = 0
    while True:
        units = sorted(units, key=lambda u: (u.pos[1], u.pos[0]))
        # print(f'Round {rn}', units)
        for u in units:
            if not u.hp > 0:
                continue

            targets = u.find_targets(units)
            if not targets:
                break

            adj_targets = u.adjacents(targets)

            # No target in range
            if not adj_targets:
                occ = walls | occupied_cells(units)
                inrange = {
                    c
                    for t in targets
                    for c in t.adjacents()
                } - occ
                path = u.find_path(inrange, occ)

                if path:
                    u.move(path[0])
                    adj_targets = u.adjacents(targets) if targets else None

            if adj_targets:
                kill = u.hit(adj_targets[0])
                if eap > 3 and kill:
                    return None

        if not targets:
            break

        rn += 1

    score = sum(u.hp for u in units if u.hp > 0)
    return rn * score


def p1(lines):
    return _solve(lines)


def p2(lines):
    for eap in range(4, 35):
        outcome = _solve(lines, eap)
        if outcome:
            return outcome


if __name__ == "__main__":
    solve(sys.argv, str_line, p1, p2)
