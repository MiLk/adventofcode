from collections.abc import Iterable
from functools import cache

from utils.file import read_input

tmap = {
    complex(x, y): int(c) if c != "." else -1
    for y, line in enumerate(read_input(__package__))
    for x, c in enumerate(line)
}

trailheads = {k for k, v in tmap.items() if v == 0}


@cache
def find_path(current: complex) -> list[list[complex]]:
    if tmap[current] == 9:
        return [[current]]

    paths = []
    for direction in [1, 1j, -1, -1j]:
        if (new := current + direction) in tmap and tmap[new] == tmap[current] + 1:
            for path in find_path(new):
                paths.append([current] + path)
    return paths


trailheads_scores = {th: set(p[-1] for p in find_path(th)) for th in trailheads}
print("Part1:", sum(len(tops) for tops in trailheads_scores.values()))

trailheads_rating = {start: set(tuple(p) for p in find_path(start)) for start in trailheads}
print("Part2:", sum(len(paths) for paths in trailheads_rating.values()))
