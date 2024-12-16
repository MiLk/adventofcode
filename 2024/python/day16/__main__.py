import math
from collections.abc import Iterable

from utils.file import read_input

lines = read_input(__package__)
walls = {complex(x, y) for y, line in enumerate(lines) for x, char in enumerate(line) if char == "#"}
start = next(complex(x, y) for y, line in enumerate(lines) for x, char in enumerate(line) if char == "S")
end = next(complex(x, y) for y, line in enumerate(lines) for x, char in enumerate(line) if char == "E")

print("Start:", start)
print("End:", end)


def neighbors(node: complex, current_direction: complex) -> Iterable[tuple[complex, complex]]:
    directions = (
        [1, -1, 1j, -1j]
        if current_direction == 0
        else [current_direction, current_direction * 1j, current_direction * -1j]
    )
    for direction in directions:
        neighbor = node + direction
        if neighbor not in walls:
            yield neighbor, direction


def walk() -> Iterable[tuple[list[complex], int]]:
    visited = {start: 0}
    # position, direction, score, path
    stack: list[tuple[complex, complex, int, list[complex]]] = [(start, 1, 0, [start])]
    while stack:
        node, current_direction, score, path = stack.pop()
        for neighbor, direction in neighbors(node, current_direction):
            new_score = score + 1 if current_direction == direction else score + 1001
            if neighbor == end:
                yield path + [neighbor], new_score
            if neighbor not in visited or new_score <= visited[neighbor]:
                stack.append((neighbor, direction, new_score, path + [neighbor]))
            else:
                pass
            visited[node] = new_score if node not in visited else min(new_score, visited[node])


walks = [list(walk())]
min_score = min(score_ for _, score_ in walks)
print("Part 1:", min_score)

best_tiles = {tile for path, score in walks if score == min_score for tile in path}
print("Part 2:", len(best_tiles))
