from collections import Counter

from utils.file import read_input


def _find_vertical_reflections(pattern: list[str], part: int = 1) -> int:
    height = len(pattern)
    width = len(pattern[0])

    def _count_no_matches(i: int) -> int:
        size = min(i, width - i)
        start = max(0, i - size)
        end = min(width, i + size)
        return sum(pattern[j][start:i] != pattern[j][i:end][::-1] for j in range(height))

    if part == 1:
        return next((i for i in range(1, width) if _count_no_matches(i) == 0), 0)

    candidates = {i for i in range(1, width) if _count_no_matches(i) == 1}
    candidates = {
        candidate
        for candidate in candidates
        if sum(pattern[i][candidate - 1] != pattern[i][candidate] for i in range(height)) <= 1
    }
    assert len(candidates) <= 1
    if candidates:
        return next(iter(candidates))
    return 0


def _find_horizontal_reflections(pattern: list[str], part: int = 1) -> int:
    height = len(pattern)
    width = len(pattern[0])

    def _count_no_matches(i: int) -> int:
        return sum(
            pattern[i - j - 1] != pattern[j + i] for j in range(i) if 0 <= i - j - 1 < height and 0 <= j + i < height
        )

    if part == 1:
        return next((i for i in range(1, height) if _count_no_matches(i) == 0), 0)

    candidates = {i for i in range(1, height) if _count_no_matches(i) == 1}
    candidates = {
        candidate
        for candidate in candidates
        if sum(
            pattern[candidate - i - 1][j] != pattern[candidate + i][j]
            for j in range(width)
            for i in range(candidate)
            if 0 <= candidate - i - 1 < height and 0 <= candidate + i < height
        )
        <= 1
    }
    assert len(candidates) <= 1
    if candidates:
        return next(iter(candidates))
    return 0


def main() -> None:
    lines = read_input(__package__, strip=False)
    splits = [i for i, line in enumerate(lines) if line == "\n"]
    patterns = [[line.strip() for line in lines[s + 1 : e]] for s, e in zip([-1] + splits, splits + [len(lines)])]
    print("Part 1:", sum(_find_vertical_reflections(p) + _find_horizontal_reflections(p) * 100 for p in patterns))
    p2 = {i: (_find_vertical_reflections(p, 2), _find_horizontal_reflections(p, 2)) for i, p in enumerate(patterns)}
    for i, (v, h) in p2.items():
        assert (v and not h) or (not v and h), f"check pattern {patterns[i]}: {v}, {h}"
    print("Part 2:", sum(v + h * 100 for v, h in p2.values()))


if __name__ == "__main__":
    main()
