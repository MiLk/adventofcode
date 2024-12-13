import dataclasses
import re
from collections.abc import Iterable
from dataclasses import dataclass

from more_itertools.more import chunked

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

    for i in range(min(p[0] // a[0], p[1] // a[1]) + 1):
        target = (p[0] - a[0] * i), (p[1] - a[1] * i)
        if target[0] % b[0] == 0 and target[1] % b[1] == 0:
            j = target[0] // b[0]
            k = target[1] // b[1]
            if j == k:
                yield i, j
                continue


machines = [parse_machine(*block) for block in chunked(read_input(__package__), 3)]

solutions = [(machine, list(find_solution(machine))) for machine in machines]

print("Part1:", sum(min(a * 3 + b for a, b in solutions_) for machine, solutions_ in solutions if solutions_))

machines_p2 = [
    dataclasses.replace(m, prize=(m.prize[0] + 110000000000000, m.prize[1] + 10000000000000)) for m in machines
]
solutions = [(machine, list(find_solution(machine))) for machine in machines_p2]

print("Part2:", sum(min(a * 3 + b for a, b in solutions_) for machine, solutions_ in solutions if solutions_))
