import dataclasses
import re
from collections.abc import Iterable
from dataclasses import dataclass

from more_itertools.more import chunked
from sympy import Eq, solve, symbols

from utils.file import read_input

BUTTON_RE = re.compile(r".*X((?:[\+-])\d+), Y((?:[\+-])\d+)$")
PRIZE_RE = re.compile(r".*X=(\d+), Y=(\d+)$")


@dataclass
class Machine:
    button_a: tuple[int, int]
    button_b: tuple[int, int]
    prize: tuple[int, int]


def parse_machine(button_a: str, button_b: str, prize: str) -> Machine:
    ma = BUTTON_RE.match(button_a)
    mb = BUTTON_RE.match(button_b)
    mp = PRIZE_RE.match(prize)
    assert ma and mb and mp
    return Machine(
        (int(ma.group(1)), int(ma.group(2))), (int(mb.group(1)), int(mb.group(2))), (int(mp.group(1)), int(mp.group(2)))
    )


def find_solution(machine: Machine) -> Iterable[tuple[int, int]]:
    a, b, p = machine.button_a, machine.button_b, machine.prize

    x, y = symbols("x, y")
    eqs = [Eq(a[i] * x + b[i] * y, p[i]) for i in range(2)]
    for solution in solve(eqs, dict=True):
        if solution[x].is_Integer and solution[y].is_Integer:
            yield solution[x], solution[y]


# I initially came up with the sympy solution for p1, because I was too lazy to think about a fast way to do it.
# I had a typo when trying to solve part 2, which leads me to rethink the whole thing,
# and after I came up with this new faster algorithm,
# I realized I had a typo in the value to add to the prize position.
def find_solution_fast(machine: Machine) -> Iterable[tuple[int, int]]:
    a, b, p = machine.button_a, machine.button_b, machine.prize

    max_iterations = min(p[0] // a[0], p[1] // a[1])
    for i in range(max_iterations + 1):
        target = (p[0] - a[0] * (max_iterations - i)), (p[1] - a[1] * (max_iterations - i))
        if target[0] % b[0] == 0 and target[1] % b[1] == 0:
            j = target[0] // b[0]
            k = target[1] // b[1]
            if j == k:
                yield (max_iterations - i), j
                continue


# This is something I wrote after looking at how other people solved the problem.
def find_solution_cramers_rule(machine: Machine) -> Iterable[tuple[int, int]]:
    a, b, p = machine.button_a, machine.button_b, machine.prize

    # a0 * x + b0 * y = p0
    # a1 * x + b1 * y = p1
    # https://en.wikipedia.org/wiki/Cramer%27s_rule
    det = a[0] * b[1] - a[1] * b[0]
    x = (p[0] * b[1] - p[1] * b[0]) / det
    y = (a[0] * p[1] - a[1] * p[0]) / det
    if x.is_integer() and y.is_integer():
        yield int(x), int(y)


machines = [parse_machine(*block) for block in chunked(read_input(__package__), 3)]

solutions = [(machine, list(find_solution_cramers_rule(machine))) for machine in machines]

print("Part1:", sum(min(a * 3 + b for a, b in solutions_) for machine, solutions_ in solutions if solutions_))

machines_p2 = [
    dataclasses.replace(m, prize=(m.prize[0] + 10000000000000, m.prize[1] + 10000000000000)) for m in machines
]
solutions = [(machine, list(find_solution_cramers_rule(machine))) for machine in machines_p2]

print("Part2:", sum(min(a * 3 + b for a, b in solutions_) for machine, solutions_ in solutions if solutions_))
