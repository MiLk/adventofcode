import queue
from functools import cache
from typing import Iterable

from utils.file import read_input

directions = {
    ">": (0, 1),
    "<": (0, -1),
    "^": (-1, 0),
    "v": (1, 0),
}


def main() -> None:
    lines = read_input(__package__)
    height = len(lines)
    width = len(lines[0])

    def next_beam(x, y, d) -> Iterable[tuple[int, int, str]]:
        if lines[x][y] == "/":
            if d == ">":
                yield x, y, "^"
            elif d == "<":
                yield x, y, "v"
            elif d == "^":
                yield x, y, ">"
            else:
                yield x, y, "<"
        elif lines[x][y] == "\\":
            if d == ">":
                yield x, y, "v"
            elif d == "<":
                yield x, y, "^"
            elif d == "^":
                yield x, y, "<"
            else:
                yield x, y, ">"
        elif lines[x][y] == "|":
            if d in {">", "<"}:
                yield x, y, "^"
                yield x, y, "v"
            else:
                yield x, y, d
        elif lines[x][y] == "-":
            if d in {"^", "v"}:
                yield x, y, "<"
                yield x, y, ">"
            else:
                yield x, y, d
        else:
            yield x, y, d

    def energize(start: tuple[int, int, str]) -> int:
        Q: queue.Queue = queue.Queue()
        Q.put(start)
        visited = set()

        while not Q.empty():
            x, y, d = Q.get()
            visited.add((x, y, d))

            dx, dy = directions[d]
            x += dx
            y += dy

            if x < 0 or x >= height or y < 0 or y >= width:
                continue

            for x, y, d in next_beam(x, y, d):
                if (x, y, d) in visited:
                    continue
                Q.put((x, y, d))

        energized = set((x, y) for x, y, _ in visited if 0 <= x < height and 0 <= y < width)
        return len(energized)

    print("Part 1:", energize((0, -1, ">")))

    configurations = set()
    for i in range(height):
        configurations.add((i, -1, ">"))
        configurations.add((i, width, "<"))
    for i in range(width):
        configurations.add((-1, i, "v"))
        configurations.add((height, i, "^"))

    energized = [(start, energize(start)) for start in configurations]
    print("Part 2:", max(energized, key=lambda x: x[1])[1])


if __name__ == "__main__":
    main()
