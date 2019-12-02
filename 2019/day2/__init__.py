#!/usr/bin/env python

import itertools

from intcode import Computer
from utils import int_list_lines

parse_input = int_list_lines(',')


def run(noun, verb, seed):
    computer = Computer(seed)
    return computer.run([(1, noun), (2, verb)])


def p1(seed):
    return run(12, 1, seed)


def p2(seed):
    return next(
        noun * 100 + verb
        for noun, verb in itertools.product(range(100), range(100))
        if run(noun, verb, seed) == 19690720
    )
