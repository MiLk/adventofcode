from typing import Tuple, List, Set, Dict

from utils import str_list_lines

parse_input = str_list_lines(',')


def resolve_path(wire: List[str]) -> Tuple[Set[Tuple[int, int]], Dict[Tuple[int, int], int]]:
    positions = set()
    costs = dict()
    x, y = 0, 0
    c = 0
    for section in wire:
        direction, length = section[0], int(section[1:])
        for i in range(length):
            if direction == 'U':
                y += 1
            elif direction == 'R':
                x += 1
            elif direction == 'D':
                y -= 1
            elif direction == 'L':
                x -= 1
            c += 1
            positions.add((x, y))
            costs[(x, y)] = c
    return positions, costs


def p1(lines: List[List[str]]) -> int:
    paths = [resolve_path(line) for line in lines]
    distances = [abs(p[0]) + abs(p[1]) for p in paths[0][0] & paths[1][0]]
    return min(distances)


def p2(lines: List[List[str]]) -> int:
    paths = [resolve_path(line) for line in lines]
    costs = [
        paths[0][1][p] + paths[1][1][p]
        for p in paths[0][0] & paths[1][0]
    ]
    return min(costs)
