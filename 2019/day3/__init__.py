from typing import Tuple, List, Dict, Iterator


def parse_input(lines: Iterator[str]) -> List[List[Tuple[int, int]]]:
    return [resolve_path(line.strip().split(",")) for line in lines]


directions: Dict[str, Tuple[int, int]] = {
    "U": (0, 1),
    "D": (0, -1),
    "L": (-1, 0),
    "R": (1, 0),
}


def resolve_path(wire: List[str]) -> List[Tuple[int, int]]:
    positions = []
    x, y = 0, 0
    for section in wire:
        direction, length = section[0], int(section[1:])
        for _ in range(length):
            x += directions[direction][0]
            y += directions[direction][1]
            positions.append((x, y))
    return positions


def p1(wires: List[List[Tuple[int, int]]]) -> int:
    return min([
        abs(p[0]) + abs(p[1])
        for p in set(wires[0]) & set(wires[1])
    ])


def p2(wires: List[List[Tuple[int, int]]]) -> int:
    return min([
        wires[0].index(p) + wires[1].index(p)
        for p in set(wires[0]) & set(wires[1])
    ])
