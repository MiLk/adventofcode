from collections import Counter
from collections.abc import Iterable
from heapq import heappop, heappush

from utils.file import read_input

lines = read_input(__package__)

height, width = len(lines), len(lines[0])

walls = {complex(x, y) for y, line in enumerate(lines) for x, char in enumerate(line) if char == "#"}
start = next(complex(x, y) for y, line in enumerate(lines) for x, char in enumerate(line) if char == "S")
end = next(complex(x, y) for y, line in enumerate(lines) for x, char in enumerate(line) if char == "E")

print("Walls:", len(walls))
print("Start:", start)
print("End:", end)


def astar(cheat: complex | None = None) -> int:
    def neighbors(current: complex) -> Iterable[complex]:
        for direction in [1, 1j, -1, -1j]:
            neighbor = current + direction
            if (
                0 <= neighbor.real < width
                and 0 <= neighbor.imag < height
                and (neighbor == cheat or neighbor not in walls)
            ):
                yield neighbor

    def heuristic(current: complex) -> int:
        return int(abs(current.real - end.real) + abs(current.imag - end.imag))

    visited: set[complex] = set()
    h: list = []
    heappush(h, (0, 0, (start.real, start.imag)))

    while h:
        _, score, node_t = heappop(h)
        node = complex(*node_t)
        if node in visited:
            continue
        if node == end:
            return score
        visited.add(node)
        for neighbor in neighbors(node):
            new_score = score + 1
            heappush(h, (new_score + heuristic(neighbor), new_score, (neighbor.real, neighbor.imag)))
    raise RuntimeError("No path found")


no_cheat = astar()
print("Benchmark:", no_cheat)

durations = {}
for i, wall in enumerate(walls):
    print("Wall:", i, "/", len(walls))
    durations[wall] = astar(wall)

c = Counter(no_cheat - duration for duration in durations.values() if duration < no_cheat)
print(sorted(c.items(), key=lambda x: x[0]))
print("Part 1:", sum(v for k, v in c.items() if k >= 100))

# def neighbors_with_cheat(current: complex, cheats_available: int) -> Iterable[complex, complex | None]:
#     for direction in [1, 1j, -1, -1j]:
#         neighbor = current + direction
#         if 0 <= neighbor.real < width and 0 <= neighbor.imag < height and neighbor not in walls:
#             yield neighbor, None
#         if cheats_available > 0:
#             yield neighbor, neighbor
#
# def walk() -> Iterable[tuple[list[complex], list[complex]]]:
#     # position, path
#     stack: list[tuple[complex, list[complex], int, list[complex]]] = [(start, [start], 1, [])]
#     while stack:
#         node, path, cheats_available, cheats = stack.pop()
#         for neighbor, cheat in neighbors_with_cheat(node, cheats_available):
#             if neighbor in path:
#                 continue
#             if neighbor == end:
#                 yield path + [neighbor], cheats
#             new_cheats_available = cheats_available - 1 if cheat else cheats_available
#             stack.append((neighbor, path + [neighbor], new_cheats_available, cheats + [cheat] if cheat else cheats))
#
# c = Counter(
#     no_cheat - duration
#     for path, _ in walk()
#     if (duration := len(path) - 1) < no_cheat
# )
# print(sorted(c.items(), key=lambda x: x[0]))
# print("Part 1:", sum(v for k, v in c.items() if k >= 100))
