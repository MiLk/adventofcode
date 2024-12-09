import math
from itertools import combinations

from black.trans import defaultdict

from utils.file import read_input

lines = read_input(__package__)

height = len(lines)
width = len(lines[0])

expected: set[complex] = set()
all_antennas: defaultdict[str, set[complex]] = defaultdict(set)
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c not in {".", "#"}:
            all_antennas[c].add(complex(x, y))
            expected.add(complex(x, y))
        if c == "#":
            expected.add(complex(x, y))

antinodes: set[complex] = set()
for frequency, antennas in all_antennas.items():
    for a, b in combinations(antennas, 2):
        diff = b - a
        antinodes.add(a - diff)
        antinodes.add(b + diff)

valid_antinodes = {a for a in antinodes if 0 <= a.real < width and 0 <= a.imag < height}
print("Part 1:", len(valid_antinodes))

antinodes_p2 = valid_antinodes.copy() | {a for antennas in all_antennas.values() for a in antennas}
for frequency, antennas in all_antennas.items():
    for a, b in combinations(antennas, 2):
        diff = b - a
        candidates = set()
        for i in range(1, min(width, height)):
            candidates.add(a - i * diff)
            candidates.add(b + i * diff)
        for candidate in candidates:
            if 0 <= candidate.real < width and 0 <= candidate.imag < height:
                antinodes_p2.add(candidate)

print("Part 2:", len(antinodes_p2))
