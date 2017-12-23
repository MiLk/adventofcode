#!/usr/bin/env python

from __future__ import print_function
from __future__ import unicode_literals


import os
import sys


def read_input(path):
    if not path:
        path = 'input.txt'
    with open(path) as f:
        lines = f.readlines()
    return lines


def process_line(line):
    return line.strip().split(' ')


def p1(lines):
    regs = dict()

    def get_value(x):
        if len(x) == 1 and ord('a') <= ord(x) <= ord('z'):
            return regs.get(x, 0)
        return int(x)

    ip = 0

    c = 0
    i = 0

    while 0 <= ip < len(lines):
        l = lines[ip]
        if l[0] == 'set':
            regs[l[1]] = get_value(l[2])
        elif l[0] == 'sub':
            regs[l[1]] = get_value(l[1]) - get_value(l[2])
        elif l[0] == 'mul':
            regs[l[1]] = get_value(l[1]) * get_value(l[2])
            c += 1
        elif l[0] == 'jnz':
            if get_value(l[1]) != 0:
                ip += get_value(l[2])
                continue
        ip += 1

    return c


def p2(init):
    h = 0
    b = int(init)
    b = b * 100
    b = b + 100000
    c = b + 17000

    while True:
        f = 1
        d = 2

        while True:
            # while e != b:
            #   e = 2
            #   if d * e - b == 0:
            #       f = 0
            if b % d == 0:
                f = 0
            d = d + 1
            if d != b:
                continue
            if f == 0:
                h = h + 1
            if b == c:
                return h
            b = b + 17
            break


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else None
    lines = read_input(path)
    lines = list(map(process_line, lines))

    s1 = p1(lines)
    print('Part 1:', s1)
    s2 = p2(lines[0][2])
    print('Part 2:', s2)


if __name__ == "__main__":
    main()
