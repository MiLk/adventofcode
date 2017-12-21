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


def flip(i):
    return [
        '/'.join(i[::-1]),
        '/'.join([l[::-1] for l in i])
    ]


def rot(i):
    if len(i) == 3:
        return [
            '/'.join([
                ''.join([i[2][0], i[1][0], i[0][0]]),
                ''.join([i[2][1], i[1][1], i[0][1]]),
                ''.join([i[2][2], i[1][2], i[0][2]])
            ]),
            '/'.join([
                ''.join([i[0][2], i[1][2], i[2][2]]),
                ''.join([i[0][1], i[1][1], i[2][1]]),
                ''.join([i[0][0], i[1][0], i[2][0]])
            ]),
            '/'.join([
                ''.join([i[2][2], i[2][1], i[2][0]]),
                ''.join([i[1][2], i[1][1], i[1][0]]),
                ''.join([i[0][2], i[0][1], i[0][0]])
            ])
        ]
    elif len(i) == 2:
        return [
            '/'.join([
                ''.join([i[1][0], i[0][0]]),
                ''.join([i[1][1], i[0][1]]),
            ]),
            '/'.join([
                ''.join([i[0][1], i[1][1]]),
                ''.join([i[0][0], i[1][0]])
            ]),
            '/'.join([
                ''.join([i[1][1], i[1][0]]),
                ''.join([i[0][1], i[0][0]])
            ])
        ]


def process_line(line):
    [i, o] = line.strip().split(' => ')
    inp = i.split('/')
    flipped = flip(inp)
    rotated = rot(inp)
    il = [i] + flipped + rotated + [f for r in rotated for f in flip(r.split('/'))]

    return map(lambda x: (x, o), il)


def get_block(pg, book, i, j, size):
    inp = '/'.join([
        pg[j + k][i:i+size]
        for k in range(size)
    ])
    return book[inp]


def convert(pg, book, size):
    s = len(pg)

    pgo = [['' for _ in range(s * (size+1) / size)] for _ in range(s * (size+1) / size)]

    for j in range(s/size):
        for i in range(s/size):
            o = get_block(pg, book, i * size, j * size, size).split('/')
            for oj in range(size + 1):
                for oi in range(size + 1):
                    pgo[j * (size+1) + oj][i * (size+1) + oi] = o[oj][oi]

    return [''.join(r) for r in pgo]


def step(pg, book):
    if len(pg) % 2 == 0:
        return convert(pg, book, 2)
    elif len(pg) % 3 == 0:
        return convert(pg, book, 3)

    return []


def solve(pg, book, p1, p2):
    s1 = 0
    for s in range(p2):
        if s == p1:
            s1 = sum([l.count('#') for l in pg])
        pg = step(pg, book)

    return s1, sum([l.count('#') for l in pg])


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else None
    lines = read_input(path)
    bookl = [r for rg in map(process_line, lines) for r in rg]
    book = dict()
    for r in bookl:
        book[r[0]] = r[1]
        print('Step:', r)

    pg = """.#.
..#
###""".split('\n')

    s1, s2 = solve(pg[:], book, 5, 18)
    print('Part 1:', s1)
    print('Part 2:', s2)


if __name__ == "__main__":
    main()
