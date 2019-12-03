from typing import Tuple, List, Set, Dict

from utils import str_list_lines

parse_input = str_list_lines(',')

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


def p1(lines: List[List[str]]) -> int:
    paths = [set(resolve_path(line)) for line in lines]
    return min([abs(p[0]) + abs(p[1]) for p in paths[0] & paths[1]])


def p2(lines: List[List[str]]) -> int:
    paths = [resolve_path(line) for line in lines]
    return min([
        paths[0].index(p) + paths[1].index(p)
        for p in set(paths[0]) & set(paths[1])
    ])
