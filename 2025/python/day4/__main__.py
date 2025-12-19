from collections.abc import Iterable
from itertools import count

from utils.file import read_input

ADJACENTS = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]


def _accessible_rolls(rolls: set[tuple[int, int]]) -> Iterable[tuple[int, int]]:
    for i, j in rolls:
        if sum(1 for dx, dy in ADJACENTS if (i + dx, j + dy) in rolls) < 4:
            yield i, j


def main() -> None:
    lines = read_input(__package__)
    height, width = len(lines), len(lines[0])
    rolls = set()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "@":
                rolls.add((x, y))
    total = 0
    for i in count():
        accessible = set(_accessible_rolls(rolls))
        removed = len(accessible)
        if i == 0:
            print("Part 1:", removed)
        if not accessible:
            break
        rolls -= accessible
        total += removed

    print("Part 2:", total)


if __name__ == "__main__":
    main()
