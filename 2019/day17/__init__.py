import itertools
from intcode import Computer
from utils import int_list_lines

parse_input = int_list_lines(',')


def p1(lines):
    computer = Computer(lines[0])
    runnable = computer.run_output()

    view = [l for l in ''.join(chr(out) for out in runnable).split('\n') if l]
    # print('\n'.join(view))

    intersections = []
    for y in range(1, len(view) - 1):

        for x in range(1, len(view[0]) - 1):
            if view[y][x] == '.':
                continue

            if any(
                view[y + j][x + i] == '.'
                for (i, j) in itertools.product([-1, 0, 1], repeat=2)
                if i == 0 or j == 0
            ):
                continue
            intersections.append((y, x))

    return sum(
        x * y for (x, y) in intersections
    )


def p2(lines):
    seed = list(lines[0])
    seed[0] = 2
    computer = Computer(seed)
    runnable = computer.run_output()

    # solved manually by looking at the view generated at part 1
    # after writing the whole sequence, find repeating sequences

    fa = ['R', '12', 'L', '10', 'R', '12']
    fb = ['L', '8', 'R', '10', 'R', '6']
    fc = ['R', '12', 'L', '10', 'R', '10', 'L', '8']
    mainseq = ['A', 'B', 'A', 'C', 'B', 'C', 'B', 'C', 'A', 'C']

    cinput = '\n'.join([
        ','.join(mainseq),
        ','.join(fa),
        ','.join(fb),
        ','.join(fc),
    ]) + '\nn\n'

    def fetch():
        for c in cinput:
            yield ord(c)

    computer.input = fetch()

    for o in runnable:
        if o > 255:
            return o

