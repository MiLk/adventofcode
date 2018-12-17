#!/usr/bin/env python

from functools import reduce

with open('grid_solved.txt') as f:
    water, dry = reduce((lambda acc, v: (acc[0] + v[0], acc[1] + v[1])), ((c == '~', c == '|') for l in f for c in l), (0, 0))
    print('Part 1:', water + dry)
    print('Part 2:', water)
