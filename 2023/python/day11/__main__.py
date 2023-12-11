from collections.abc import Iterable
from itertools import combinations

from utils.file import read_input


def expand_galaxies(
    galaxies: list[tuple[int, int]], columns_to_expand: set[int], rows_to_expand: set[int], factor: int
) -> list[tuple[int, int]]:
    return [
        (
            r + sum(er < r for er in rows_to_expand) * (factor - 1),
            c + sum(ec < c for ec in columns_to_expand) * (factor - 1),
        )
        for r, c in galaxies
    ]


def solve(galaxies: list[tuple[int, int]]) -> int:
    return sum(abs(ar - br) + abs(ac - bc) for (ar, ac), (br, bc) in combinations(galaxies, 2))


def main() -> None:
    image = read_input(__package__)
    columns_to_expand = {c for c in range(len(image)) if all(image[r][c] == "." for r in range(len(image)))}
    rows_to_expand = {r for r, line in enumerate(image) if all(c == "." for c in line)}
    galaxies = [(r, c) for r in range(len(image)) for c in range(len(image[r])) if image[r][c] == "#"]
    for i, factor in enumerate([2, 1_000_000], start=1):
        print(f"Part {i}: {solve(expand_galaxies(galaxies, columns_to_expand, rows_to_expand, factor))}")


if __name__ == "__main__":
    main()
