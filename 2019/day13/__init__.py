import itertools

from intcode import Computer
from utils import int_list_lines

parse_input = int_list_lines(',')


def p1(lines):
    screen = dict()
    computer = Computer(lines[0])
    runnable = computer.run_output()

    try:
        while True:
            x, y, tile_id = next(runnable), next(runnable), next(runnable)
            screen[(x, y)] = tile_id
    except StopIteration:
        pass

    return sum(t == 2 for t in screen.values())


def p2(lines):
    screen = dict()
    score = 0

    def fetch():
        while True:
            ball = next((k for k, v in screen.items() if v == 4), None)
            paddle = next((k for k, v in screen.items() if v == 3), None)
            if not ball or not paddle:
                yield 0
            if ball[0] < paddle[0]:
                yield -1
            elif ball[0] > paddle[0]:
                yield 1
            else:
                yield 0

    seed = list(lines[0])
    seed[0] = 2
    computer = Computer(seed)
    computer.input = fetch()
    runnable = computer.run_output()

    try:
        while True:
            x, y, tile_id = next(runnable), next(runnable), next(runnable)
            if x == -1 and y == 0:
                score = tile_id
            else:
                screen[(x, y)] = tile_id
    except StopIteration:
        pass

    return score
