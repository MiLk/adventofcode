from collections import defaultdict

from utils.file import read_input

DIRECTIONS = {
    "U": -1j,
    "D": 1j,
    "L": -1,
    "R": 1,
}

ENCODED_DIRECTIONS = ["R", "D", "L", "U"]


def parse_line(line: str) -> tuple[str, int, str, int]:
    direction, distance, color = line.split(" ", maxsplit=2)
    direction2, distance2 = ENCODED_DIRECTIONS[int(color[7])], int(color[2:7], 16)
    return direction, int(distance), direction2, distance2


def main() -> None:
    instructions = [parse_line(line) for line in read_input(__package__)]
    current = 0
    trench: set[complex] = set()
    for direction, distance, *_ in instructions:
        for _ in range(distance):
            current += DIRECTIONS[direction]
            trench.add(current)
    # min_x = int(min(trench, key=lambda c: c.real).real)
    # max_x = int(max(trench, key=lambda c: c.real).real)
    # min_y = int(min(trench, key=lambda c: c.imag).imag)
    # max_y = int(max(trench, key=lambda c: c.imag).imag)

    # for r in range(min_y, max_y + 1):
    #     print(str(r) + "\t", end=' ')
    #     for c in range(min_x, max_x + 1):
    #         xy = c + r * 1j
    #         if xy in trench:
    #             print('#', end='')
    #         else:
    #             print('.', end='')
    #     print()

    # observation from drawing
    fill_start = 42 - 236j
    interior = set()

    Q = [fill_start]
    while Q:
        xy = Q.pop()
        interior.add(xy)
        for d in DIRECTIONS.values():
            n = xy + d
            if n not in trench and n not in interior:
                Q.append(n)

    # for r in range(min_y, max_y + 1):
    #     print(str(r) + "\t", end=' ')
    #     for c in range(min_x, max_x + 1):
    #         xy = c + r * 1j
    #         if xy in trench:
    #             print('#', end='')
    #         elif xy in interior:
    #             print('X', end='')
    #         else:
    #             print('.', end='')
    #     print()

    print("Part 1:", len(interior) + len(trench))


if __name__ == "__main__":
    main()
