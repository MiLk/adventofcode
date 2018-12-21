#!/usr/bin/env python

import os
import sys

sys.path.insert(0, os.path.abspath('../..'))

from utils import solve  # nopep8


def terminate(part1=True):
    r2 = 0
    seen = set()
    p = 0
    while True:
        r4 = r2 | 0x10000  # 6
        r2 = 6718165       # 7

        i = 0
        while True:
            r3 = r4 & 0xff  # 8
            r2 = (((r2 + r3) & 0xffffff) * 65899) & 0xffffff  # 9 - 12
            if 256 > r4:  # 13 - 16
                break
            r4, _ = divmod(r4, 256)  # 17 - 26
            i += 1

        if part1:
            return r2
        if r2 in seen:
            return p
        seen.add(r2)
        p = r2


def p1(_):
    return terminate()


def p2(_):
    return terminate(False)


if __name__ == "__main__":
    solve([], lambda x: x, p1, p2)
