import itertools
from functools import lru_cache

from intcode import Computer
from utils import int_list_lines

parse_input = int_list_lines(',')


def p1(lines):
    out = 0
    for x, y in itertools.product(range(50), range(50)):
        computer = Computer(lines[0])
        runnable = computer.run_output()
        computer.input = iter([x, y])
        if next(runnable):
            out += 1
    return out


def p2(lines):
    @lru_cache(maxsize=1024*1024)
    def is_beam(x, y):
        computer = Computer(lines[0])
        runnable = computer.run_output()
        computer.input = iter([x, y])
        return next(runnable, 0) == 1

    x = 0
    for y in range(950, 1100):
        x = max(x - 3, 0)
        while not is_beam(x, y):
            x += 1

        corners = is_beam(x + 99, y), is_beam(x, y - 99), is_beam(x + 99, y - 99)
        if sum(corners) == 3:
            return x * 10000 + y - 99
