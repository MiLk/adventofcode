from collections.abc import Iterable, Container
from heapq import heappush, heappop

from utils.file import read_input, int_list_line

falling_bytes = [complex(x,y) for x,y in (int_list_line(line, ",") for line in read_input(__package__))]
start = 0j
goal = 70+70j if len(falling_bytes) > 50 else 6+6j


def astar(corruption_size: int) -> int:
    corrupted = set(falling_bytes[:corruption_size])

    def neighbors(current: complex) -> Iterable[complex]:
        for direction in [1, 1j, -1, -1j]:
            neighbor = current + direction
            if 0 <= neighbor.real <= goal.real and 0 <= neighbor.imag <= goal.imag and neighbor not in corrupted:
                yield neighbor

    def heuristic(current: complex) -> int:
        return int(abs(current.real - goal.real) + abs(current.imag - goal.imag))

    best_score = None
    visited = {}
    h = []
    heappush(h, (0, 0, (start.real, start.imag)))

    while h:
        _, score, node_t = heappop(h)
        node = complex(*node_t)
        if node in visited:
            continue
        if node == goal:
            return score
        visited[node] = score if node not in visited else min(score, visited[node])
        for neighbor in neighbors(node):
            new_score = score + 1
            heappush(h, (new_score + heuristic(neighbor), new_score, (neighbor.real, neighbor.imag)))
    raise RuntimeError("No path found")

print("Part 1:", astar(1024))
