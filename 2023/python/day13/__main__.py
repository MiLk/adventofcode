from collections.abc import Iterable
from itertools import combinations

from utils.file import read_input


def _find_vertical_reflections(pattern: list[str]) -> int:
    height = len(pattern)
    width = len(pattern[0])
    for i in range(1, width):
        size = min(i, width - i)
        start = max(0, i - size)
        end = min(width, i + size)
        if all(pattern[j][start:i] == pattern[j][i:end][::-1] for j in range(height)):
            return i
    return 0


def _find_horizontal_reflections(pattern: list[str]) -> int:
    height = len(pattern)
    for i in range(1, height):
        if all(
            pattern[i - j - 1] == pattern[j + i] for j in range(i) if 0 <= i - j - 1 < height and 0 <= j + i < height
        ):
            return i
    return 0


def main() -> None:
    lines = read_input(__package__, strip=False)
    splits = [i for i, line in enumerate(lines) if line == "\n"]
    patterns = [[line.strip() for line in lines[s + 1 : e]] for s, e in zip([-1] + splits, splits + [len(lines)])]
    print("Part 1:", sum(_find_vertical_reflections(p) + _find_horizontal_reflections(p) * 100 for p in patterns))


if __name__ == "__main__":
    main()
