import operator
import re
from functools import reduce

from utils.file import read_input

DIGITS_RE = re.compile(r"\d+")


def is_adjacent_to_symbol(chars: set[tuple[int, int]], ln: int, start: int, end: int):
    return any((i, j) in chars for i in range(ln - 1, ln + 2) for j in range(start - 1, end + 1))


def main() -> None:
    lines = read_input()
    size = len(lines)

    chars: set[tuple[int, int]] = {(i, j) for i in range(size) for j in range(size) if lines[i][j] not in "0123456789."}

    parts: list[tuple[int, tuple[int, int, int]]] = [
        (int(m.group()), (ln, m.start(), m.end()))
        for ln, line in enumerate(lines)
        for m in DIGITS_RE.finditer(line)
        if is_adjacent_to_symbol(chars, ln, m.start(), m.end())
    ]

    print("Part 1:", sum(p[0] for p in parts))

    parts_coords = {(i, j): n for n, (i, js, je) in parts for j in range(js, je)}

    gears = (
        reduce(operator.mul, ps, 1)
        for (ci, cj) in chars
        if lines[ci][cj] == "*"
        and (
            ps := set(
                part_number
                for i in range(ci - 1, ci + 2)
                for j in range(cj - 1, cj + 2)
                if (part_number := parts_coords.get((i, j)))
            )
        )
        if len(ps) == 2
    )

    print("Part 2:", sum(gears))


if __name__ == "__main__":
    main()
