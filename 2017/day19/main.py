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


def get_cell(path, i, j):
    if i < 0 or j < 0:
        return ' '
    if j >= len(path):
        return ' '
    if i >= len(path[j]):
        return ' '
    return path[j][i]


def cross(i, j, dir, path):
    if dir == 'D' and get_cell(path, i, j + 1) != ' ':
        return 'D'

    if dir == 'U' and get_cell(path, i, j - 1) != ' ':
        return 'U'

    if dir == 'L' and get_cell(path, i - 1, j) != ' ':
        return 'L'

    if dir == 'R' and get_cell(path, i + 1, j) != ' ':
        return 'R'

    if dir == 'D' or dir == 'U':
        if get_cell(path, i - 1, j) != ' ':
            return 'L'
        elif get_cell(path, i + 1, j) != ' ':
            return 'R'

    if dir == 'L' or dir == 'R':
        if get_cell(path, i, j + 1) != ' ':
            return 'D'
        elif get_cell(path, i, j - 1) != ' ':
            return 'U'

    return None


def debug(path, i, j, size=5):
    l = (size - 1) / 2
    print('\t', '\t'.join(["%d" % ii for ii in range(i-l, i+l+1)]))
    for jj in range(j-l, j+l+1):
        print(jj, '\t', '\t'.join([get_cell(path, ii, jj) for ii in range(i-l, i+l+1)]))


def p1(path):
    i, j = 1, 0
    dir = 'D'

    letters = []

    debug(path, i, j)

    steps = 0

    while True:
        c = path[j][i]
        if c == ' ' or c == '\n':
            print('stop', i, j, c, dir)
            debug(path, i, j, 7)
            break
        elif c == '|':
            pass
        elif c == '-':
            pass
        elif c == '+':
            dir = cross(i, j, dir, path)
            if not dir:
                raise Exception('Wrong dir')
        else:
            letters.append(c)

        if dir == 'D':
            j += 1
        elif dir == 'U':
            j -= 1
        elif dir == 'L':
            i -= 1
        elif dir == 'R':
            i += 1
        steps += 1

    return ''.join(letters), steps


def p2(line):
    return line


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else None
    lines = [l.strip('\n') for l in read_input(path)]

    s1, s2 = p1(lines)
    print('Part 1:', s1)
    print('Part 2:', s2)


if __name__ == "__main__":
    main()
