#!/usr/bin/env python

import itertools
import os
import sys
from collections import defaultdict
import functools
import heapq

sys.path.insert(0, os.path.abspath('../..'))

from utils import solve, int_line, int_list_line, str_line, str_list_line  # nopep8


target = None


def geologic_index(x, y, depth):
    global target
    if (x, y) == (0, 0):
        return 0

    if (x, y) == target:
        return 0

    if y == 0:
        return x * 16807

    if x == 0:
        return y * 48271

    return erosion_level((x - 1, y), depth) * erosion_level((x, y -1), depth)


@functools.lru_cache(None)
def erosion_level(pos, depth):
    return (geologic_index(*pos, depth) + depth) % 20183


def region_type(pos, depth):
    return erosion_level(pos, depth) % 3


def p1(lines):
    global target
    depth = lines[0]
    target = lines[1]

    return sum(
        region_type((i, j), depth)
        for i, j in itertools.product(range(target[0] + 1), range(target[1] + 1))
    )


def p2(lines):
    depth = lines[0]
    target = (lines[1][0], lines[1][1], 1)

    # neither: 0
    # torch: 1
    # climbing gear: 2
    queue = [(0, 0, 0, 1)]  # (minutes, x, y, type)
    timings = dict()  # (x, y, type) : minutes

    while queue:
        minutes, x, y, currentGear = heapq.heappop(queue)
        pos = (x, y, currentGear)
        if pos in timings and timings[pos] <= minutes:
            continue
        timings[pos] = minutes
        if pos == target:
            return minutes

        for gearId in range(3):
            # Can't equip already equipped gear
            if gearId == currentGear:
                continue
            # Can't equip gear in the current region
            if gearId == region_type((x, y), depth):
                continue
            heapq.heappush(queue, (minutes + 7, x, y, gearId))

        # try going up down left right
        for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            newx = x + dx
            newy = y + dy
            if newx < 0:
                continue
            if newy < 0:
                continue
            # Can't go to this region with the current gear
            if region_type((newx, newy), depth) == currentGear:
                continue
            heapq.heappush(queue, (minutes + 1, newx, newy, currentGear))


if __name__ == "__main__":
    solve([11394, (7, 701)], lambda x: x, p1, p2)
