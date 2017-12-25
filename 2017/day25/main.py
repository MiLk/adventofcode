#!/usr/bin/env python

from __future__ import print_function
from __future__ import unicode_literals


from builtins import range
import collections


def solve():
    tape = collections.defaultdict(int)
    cursor = 0
    state = 'A'
    checksum_after = 12173597

    for step in range(checksum_after + 1):
        if tape[cursor] == 0:
            tape[cursor] = 1
            if state in ['A', 'C', 'D', 'F']:
                cursor += 1
            else:
                cursor -= 1
            if state == 'A':
                state = 'B'
            elif state == 'E':
                state = 'F'
            elif state == 'F':
                state = 'D'
            else:
                state = 'A'
        else:
            if state in ['A', 'C', 'D']:
                tape[cursor] = 0
            if state in ['B', 'D', 'F']:
                cursor += 1
            else:
                cursor -= 1
            if state == 'B':
                state = 'D'
            elif state == 'C':
                state = 'E'
            elif state == 'D':
                state = 'B'
            elif state == 'F':
                state = 'A'
            else:
                state = 'C'
        if step % 1000000 == 0:
            print(step, '/', checksum_after)

    return sum(tape.values())


def main():
    print(solve())


if __name__ == "__main__":
    main()
