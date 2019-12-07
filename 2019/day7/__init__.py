import itertools

from intcode import Computer
from utils import int_list_lines

parse_input = int_list_lines(',')


def compute(lines, permutation):
    signal = 0
    for phase in permutation:
        computer = Computer(lines[0])
        computer.input = iter([phase, signal])
        computer.run_mode()
        signal = computer.output
    return signal


def p1(lines):
    permutations = itertools.permutations(list(range(5)))
    return max(
        compute(lines, permutation)
        for permutation in permutations
    )


def compute2(lines, permutation):
    inputs = {}
    runnable = {}

    def fetch(idx):
        return (inputs[idx][i] for i in itertools.count())

    for idx, phase in enumerate(permutation):
        c = Computer(lines[0])
        c.input = fetch(idx)
        inputs[idx] = [phase]
        runnable[idx] = c.run_output()
    inputs[0].append(0)

    while True:
        for n, r in runnable.items():
            try:
                out = next(r)
            except StopIteration:
                return out
            inputs[(n+1) % 5].append(out)


def p2(lines):
    permutations = itertools.permutations(list([n + 5 for n in range(5)]))
    return max(
        compute2(lines, permutation)
        for permutation in permutations
    )
