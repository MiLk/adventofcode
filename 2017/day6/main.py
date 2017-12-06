#!/usr/bin/env python

from __future__ import print_function
from __future__ import unicode_literals

import sys


def read_input(path):
    if not path:
        path = 'input.txt'
    with open(path) as f:
        lines = f.readlines()
    return lines


def process_line(line):
    return zip(
        tuple(range(0, 16)),
        tuple([int(n) for n in line.strip().split('\t')])
    )


def execute_step(blocks, m):
    blocks[m[0]] = (m[0], 0)
    for j in range(0, m[1]):
        idx = (m[0] + j + 1) % 16
        blocks[idx] = (idx, blocks[idx][1] + 1)
    return blocks


def execute(blocks):
    i = 0
    seen = []
    while blocks not in seen:
        seen.append(blocks)
        m = max(blocks, key=lambda x: x[1])
        blocks = tuple(execute_step(list(blocks), m))
        i += 1

    return i, blocks


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else None
    blocks = process_line(read_input(path)[0])

    s1, blocks = execute(blocks)
    print('Part 1:', s1)

    s2, _ = execute(blocks)
    print('Part 2:', s2)


if __name__ == "__main__":
    main()
