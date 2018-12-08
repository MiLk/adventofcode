#!/usr/bin/env python

import os
import sys

sys.path.insert(0, os.path.abspath('../..'))

from utils import solve, int_list_line  # nopep8


class Node:
    children = []
    metadata = []

    def __init__(self, c, m):
        self.children = c
        self.metadata = m

    @staticmethod
    def create(l):
        nn = next(l)
        mn = next(l)
        children = []
        for _ in range(0, nn):
            c = Node.create(l)
            children.append(c)
        n = Node(children, [next(l) for _ in range(0, mn)])
        return n

    def metadata_sum(self):
        return sum(self.metadata) + sum(c.metadata_sum() for c in self.children)

    def value(self):
        if len(self.children) == 0:
            return sum(self.metadata)
        return sum(
            self.children[i - 1].value()
            for i in self.metadata
            if i <= len(self.children)
        )


def p1(lines):
    tree = Node.create(iter(lines[0]))
    return tree.metadata_sum()


def p2(lines):
    tree = Node.create(iter(lines[0]))
    return tree.value()


if __name__ == "__main__":
    solve(sys.argv, lambda l: int_list_line(l, ' '), p1, p2)
