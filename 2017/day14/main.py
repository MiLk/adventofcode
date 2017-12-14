#!/usr/bin/env python

from __future__ import print_function
from __future__ import unicode_literals

import sys

from builtins import range
import binascii


def read_input(path):
    if not path:
        path = 'input.txt'
    with open(path) as f:
        lines = f.readlines()
    return lines


def process_line(line):
    return [int(n) for n in line.strip().split('\t')]


def solve_hash(size, ls, r=1):
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


def hash(string):
    return dense(solve_hash(256, map(ord, string) + [17, 31, 73, 47, 23], 64))


def solve(line):
    used = 0

    disk = []

    for row in range(128):
        hin = "%s-%d" % (line, row)
        hout = hash(hin)
        bout = (bin(int(hout, 16)))[2:].zfill(128)
        disk.append(map(int, bout))
        used += bout.count('1')

    return used, p2(disk)


def p2(disk):
    seen = set()
    n = 0

    def explore(i, j):
        if (i, j) in seen:
            return
        if disk[i][j] == 0:
            return
        seen.add((i, j))
        if i > 0:
            explore(i-1, j)
        if j > 0:
            explore(i, j-1)
        if i < 127:
            explore(i+1, j)
        if j < 127:
            explore(i, j+1)

    for i in range(128):
        for j in range(128):
            if (i, j) in seen:
                continue
            if disk[i][j] == 0:
                continue
            n += 1
            explore(i, j)

    return n


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else None
    lines = read_input(path)[0].strip()

    s1, s2 = solve(lines)
    print('Part 1:', s1)
    print('Part 2:', s2)


if __name__ == "__main__":
    main()
