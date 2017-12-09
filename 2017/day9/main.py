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
    return [int(n) for n in line.strip().split('\t')]


def solve(stream):
    """
    >>> solve('{}')
    (1, 0)
    >>> solve('{{{}}}')
    (6, 0)
    >>> solve('{{},{}}')
    (5, 0)
    >>> solve('{{{},{},{{}}}}')
    (16, 0)
    >>> solve('{{<ab>},{<ab>},{<ab>},{<ab>}}')
    (9, 8)
    >>> solve('{{<!!>},{<!!>},{<!!>},{<!!>}}')
    (9, 0)
    """

    i = 0
    groups = dict()
    idx = 0
    current = 0
    parent = 0
    depth = 0
    is_garbage = False
    removed = 0
    while i < len(stream):
        c = stream[i]
        if is_garbage and c == '>':
            is_garbage = False
        elif is_garbage and c == '!':
            i += 1
        elif is_garbage:
            removed += 1
        elif c == '{':
            parent = current
            current = idx
            depth += 1
            groups[current] = [parent, depth, 0]
            idx += 1
        elif c == '}':
            if parent != current:
                groups[parent][2] += depth + groups[current][2]
            current = parent
            parent = groups[current][0]
            depth -= 1
        elif c == '<':
            is_garbage = True
        i += 1
    return groups[0][1] + groups[0][2], removed


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else None
    stream = read_input(path)[0].strip()

    s1, s2 = solve(stream)
    print('Part 1:', s1)
    print('Part 2:', s2)


if __name__ == "__main__":
    main()
