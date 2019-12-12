import itertools
import math

from utils import int_lines, int_list_lines, str_lines, str_list_lines
import re

PATTERN = re.compile(r"^<x=(-?\d+), y=(-?\d+), z=(-?\d+)>$")


def parse_input(lines):
    return [
        tuple([int(n) for n in re.match(PATTERN, l).groups()])
        for l in lines
    ]


def process_step(positions, velocity):
    # Apply gravity
    for i, j in itertools.combinations(range(len(positions)), 2):
        for k in range(3):
            if positions[i][k] > positions[j][k]:
                velocity[i][k] -= 1
                velocity[j][k] += 1
            elif positions[i][k] < positions[j][k]:
                velocity[i][k] += 1
                velocity[j][k] -= 1
    # Apply velocity
    for i in range(len(positions)):
        p, v = positions[i], velocity[i]
        positions[i] = tuple(p[k] + v[k] for k in range(3))


def p1(start):
    positions = list(start)
    velocity = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for _ in range(1000):
        process_step(positions, velocity)

    return sum(
        sum(abs(n) for n in positions[m]) * sum(abs(n) for n in velocity[m])
        for m in range(len(positions))
    )


def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b // math.gcd(a, b)


def p2(start):
    rep = [0, 0, 0]
    positions = list(start)
    velocity = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    seen = [tuple([p[i] for p in positions] + [v[i] for v in velocity]) for i in range(3)]

    for step in itertools.count():
        process_step(positions, velocity)

        for i in range(3):
            if rep[i] != 0:
                continue
            snapshot = tuple([p[i] for p in positions] + [v[i] for v in velocity])
            if snapshot == seen[i]:
                rep[i] = step + 1

        if all(n != 0 for n in rep):
            return lcm(lcm(rep[0], rep[1]), rep[2])
