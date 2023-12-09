import re
from collections import defaultdict
from itertools import cycle
from math import lcm
from typing import Callable

from utils.file import read_input

NODE_RE = re.compile(r"^(\w{3}) = \((\w{3}), (\w{3})\)$")


def parse_line(line: str) -> tuple[str, tuple[str, str]]:
    m = NODE_RE.match(line)
    assert m
    return m.group(1), (m.group(2), m.group(3))


def navigate(
    nodes: dict[str, tuple[str, str]],
    instructions: str,
    start: str,
    end_predicate: Callable[[str], bool],
    find_cycle: bool = False,
) -> int:
    cycles: list[int] = []
    current_node = start
    for step, instruction in enumerate(cycle(instructions), start=1):
        current_node = nodes[current_node][0 if instruction == "L" else 1]
        if end_predicate(current_node):
            if not find_cycle:
                return step
            # Only used to verify that the cycle is regular
            cycles.append(step)
            if len(cycles) == 10:
                diff = [b - a for a, b in zip(cycles, cycles[1:])]
                print(start, current_node, cycles, diff)
                return cycles[0]
    return 0


def main() -> None:
    lines = read_input(__package__)
    instructions = lines[0]
    nodes: dict[str, tuple[str, str]] = dict(map(parse_line, lines[1:]))

    print("Part1:", navigate(nodes, instructions, "AAA", lambda n: n == "ZZZ"))

    start_nodes = [n for n in nodes if n[2] == "A"]
    cycle_sizes = [navigate(nodes, instructions, node, lambda n: n[2] == "Z") for node in start_nodes]
    print("Part2:", lcm(*cycle_sizes))


if __name__ == "__main__":
    main()
