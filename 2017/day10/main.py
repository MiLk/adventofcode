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


def solve(size, ls, r=1):
    ns = list(range(size))
    current = 0
    skip = 0

    for _ in range(r):
        for l in ls:
            if l > size:
                continue
            st = current % size
            if st + l > size:
                end = st + l - size
                s1 = ns[st:]
                s2 = ns[:end]
                s = s1 + s2
                s = s[::-1]
                ns[st:] = s[:size - st]
                ns[:end] = s[size - st:]
            else:
                s = ns[st:st+l]
                ns[st:st+l] = s[::-1]
            current += l + skip
            skip += 1
    return ns[:]


def xor(l):
    num = 0
    for i in range(16):
        num ^= l[i]
    return num


def dense(h):
    return ''.join([
        hex(xor(h[i * 16:(i + 1) * 16]))[2:].zfill(2)
        for i in range(16)
    ])


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else None
    lines = read_input(path)[0].strip()

    s1 = solve(256, map(int, lines.split(',')))
    print('Part 1:', s1[0] * s1[1])

    s2 = solve(256, map(ord, lines) + [17, 31, 73, 47, 23], 64)
    print('Part 2:', dense(s2))


if __name__ == "__main__":
    main()
