import itertools
from collections import defaultdict, Counter
from math import gcd, atan2

from utils import str_lines

parse_input = str_lines


def can_detect(a, b, asteroids):
    dx, dy = b[0] - a[0], b[1] - a[1]
    if dy == 0:
        step_x, step_y = dx / abs(dx), 0
        n = abs(dx)
    elif dx == 0:
        step_x, step_y = 0, dy / abs(dy)
        n = abs(dy)
    else:
        g = abs(gcd(dy, dx))
        step_x, step_y = dx / g, dy / g
        n = g

    for i in range(1, n):
        p = (a[0] + step_x * i, a[1] + step_y * i)
        if p in asteroids:
            return False
    return True


def p1(lines):
    asteroids = {
        (i, j)
        for i, j in itertools.product(range(len(lines[0])), range(len(lines)))
        if lines[j][i] == '#'
    }

    visible = {
        a: len([b for b in asteroids if a != b and can_detect(a, b, asteroids)])
        for a in asteroids
    }
    return Counter(visible).most_common()[0][1]


def p2(lines):
    asteroids = {
        (i, j)
        for i, j in itertools.product(range(len(lines[0])), range(len(lines)))
        if lines[j][i] == '#'
    }
    laser = (27, 19)
    destroyed = []
    while len(destroyed) < 200:
        angles = sorted([
            # atan2(x, y) is the angle between the positive y-axis and the way to the point (x,y)
            (atan2(target[0] - laser[0], target[1] - laser[1]), target)
            for target in asteroids
            if laser != target and can_detect(laser, target, asteroids - set(destroyed))

        ], reverse=True)
        destroyed.extend(t for _, t in angles)
    return destroyed[199][0] + destroyed[199][1] * 100
