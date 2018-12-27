#!/usr/bin/env python

import os
import sys
from collections import defaultdict
import heapq

sys.path.insert(0, os.path.abspath('../..'))

from utils import solve, int_list_line  # nopep8


def dist(u, v):
    return sum(abs(u[i] - v[i]) for i in range(len(u)))


def p1(lines):
    connections = defaultdict(set)
    for i in range(len(lines)):
        for j in range(len(lines)):
            if j <= i:
                continue
            u, v = lines[i], lines[j]
            if dist(u, v) > 3:
                continue
            connections[u].add(v)
            connections[v].add(u)

    resolved = set()
    constellations = 0

    for star in lines:
        if star in resolved:
            continue

        constellations += 1
        q = [star]
        while q:
            u = heapq.heappop(q)
            if u in resolved:
                continue
            resolved.add(u)
            for v in connections[u]:
                if v not in resolved:
                    heapq.heappush(q, v)
    return constellations


def p2(_):
    return None


if __name__ == "__main__":
    solve(sys.argv, lambda l: tuple(int_list_line(l, ',')), p1, p2)
