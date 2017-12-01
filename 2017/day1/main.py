#!/usr/bin/env python

from __future__ import print_function
from __future__ import unicode_literals

import sys


def get_sum(digits, offset):
    l = len(digits)
    return sum([
        digits[i % l]
        for i in xrange(0, l)
        if digits[i % l] == digits[(i + offset) % l]
    ])


def main():
    digits = [int(d) for d in sys.argv[1]]

    print('Part 1: %d' % get_sum(digits, 1))
    print('Part 2: %d' % get_sum(digits, len(digits)/2))


if __name__ == "__main__":
    main()
