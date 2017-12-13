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
    s = line.strip().split(': ')
    return int(s[0]), int(s[1])


def scanner(range, time):
    return time % (2 * (range - 1)) == 0


def severity(firewall):
    s = 0
    for d in firewall.keys():
        r = firewall[d]
        if scanner(r, d):
            s += d * r
    return s


def allowed(firewall, start=0):
    for d in firewall.keys():
        r = firewall[d]
        if scanner(r, d + start):
            return False
    return True


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else None
    lines = read_input(path)
    lines = map(process_line, lines)
    firewall = dict(lines)

    s1 = severity(firewall)
    print('Part 1:', s1)

    s2 = 0
    while not allowed(firewall, s2):
        s2 += 1
    print('Part 2:', s2)


if __name__ == "__main__":
    main()
