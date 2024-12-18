from collections.abc import Iterable, Container

from utils.file import read_input, int_list_line

falling_bytes = [complex(x,y) for x,y in (int_list_line(line, ",") for line in read_input(__package__))]
start = 0j
goal = 70+70j if len(falling_bytes) > 50 else 6+6j

def neighbors(node: complex, walls: Container[complex]) -> Iterable[complex]:
    for direction in [1, -1, 1j, -1j]:
        neighbor = node + direction
        if neighbor.real < 0 or neighbor.imag < 0 or neighbor.real > goal.real or neighbor.imag > goal.imag:
            continue
        if neighbor not in walls:
            yield neighbor

def heuristic(node: complex, goal: complex) -> int:
    return int(abs(node.real - goal.real) + abs(node.imag - goal.imag)) + int(abs(node.real - node.imag))

def walk(corruption_size: int) -> Iterable[tuple[list[complex], int]]:
    corrupted = set(falling_bytes[:corruption_size])
    best_score = None
    visited = {start: 0}
    # position, score, path
    stack: list[tuple[complex, int, list[complex]]] = [(start, 0, [start])]
    while stack:
        stack.sort(key=lambda x: x[1] + heuristic(x[0], goal))
        node, score, path = stack.pop()
        if score > best_score:
            continue
        visited[node] = score if node not in visited else min(score, visited[node])
        for neighbor in neighbors(node, corrupted):
            new_score = score + 1
            if neighbor == goal:
                #print("Path found", new_score, len(stack))
                best_score = min(best_score, new_score) if best_score else new_score
                yield path + [neighbor], new_score
            if neighbor not in visited or new_score < visited[neighbor]:
                stack.append((neighbor, new_score, path + [neighbor]))

paths = list(walk(1024))
print("Part 1:", min(score for path, score in paths))
