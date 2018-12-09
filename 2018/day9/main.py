#!/usr/bin/env python

import os
import sys
from collections import defaultdict

sys.path.insert(0, os.path.abspath('../..'))

from utils import solve  # nopep8


class Circle:
    placed = []
    left = set()
    current = None

    def __init__(self, last):

        self.placed = [0]
        self.current = 0
        self.left = set(i for i in range(1, last + 1))

    def place(self):
        m = min(self.left)
        if m % 23 == 0:
            return self.place23(m)

        if len(self.placed) in [1, 2]:
            l = 1
        elif self.current == len(self.placed) - 1:
            l = 1
        else:
            l = (self.current + 2) % (len(self.placed) + 1)
        self.placed.insert(l, m)
        self.left.remove(m)
        self.current = l
        return 0

    def place23(self, m):
        l = (self.current - 7) % len(self.placed)
        s = m + self.placed.pop(l)
        self.left.remove(m)
        self.current = l
        return s


def p1(lines):
    p, last = lines
    scores = defaultdict(int)
    current_p = 0
    circle = Circle(last)
    while len(circle.left) > 0:
        score = circle.place()
        scores[current_p] += score
        current_p = (current_p + 1) % p

    return max(scores.values())


def p2(_):
    return None


if __name__ == "__main__":
    solve((424, 71482), lambda x: x, p1, p2)
