#!/usr/bin/env python

from __future__ import print_function
from __future__ import unicode_literals

import sys


def get_sum(digits, offset):
    l = len(digits)
    match = []

    i = 0
    while i < l:
        if digits[i % l] == digits[(i + offset) % l]:
            match.append(digits[i % l])
        i += 1

    return sum(match)


def main():
    digits = [int(d) for d in sys.argv[1]]

    print('Part 1: %d' % get_sum(digits, 1))
    print('Part 2: %d' % get_sum(digits, len(digits)/2))


if __name__ == "__main__":
    main()
