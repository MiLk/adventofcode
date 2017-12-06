#!/usr/bin/env python

from __future__ import print_function
from __future__ import unicode_literals

import sys

from builtins import range


def read_input(path):
    if not path:
        path = 'input.txt'
    with open(path) as f:
        lines = f.readlines()
    return lines


def process_line(line):
    return tuple([int(n) for n in line.strip().split('\t')])


def execute_step(blocks, m):
    to_spread, blocks[m] = blocks[m], 0
    for i in range(to_spread):
        blocks[(m + i + 1) % len(blocks)] += 1
    return blocks


def execute(blocks):
    seen = []
    while blocks not in seen:
        seen.append(blocks)
        blocks = tuple(execute_step(list(blocks), blocks.index(max(blocks))))
    return len(seen), blocks


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else None
    blocks = process_line(read_input(path)[0])

    s1, blocks = execute(blocks)
    print('Part 1:', s1)

    s2, _ = execute(blocks)
    print('Part 2:', s2)


if __name__ == "__main__":
    main()
