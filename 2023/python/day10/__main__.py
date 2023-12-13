from utils.file import read_input

directions: dict[str, tuple[int, int]] = {"N": (-1, 0), "E": (0, 1), "S": (1, 0), "W": (0, -1)}

tiles: dict[str, list[tuple[int, int]]] = {
    "|": [directions["N"], directions["S"]],
    "-": [directions["E"], directions["W"]],
    "L": [directions["N"], directions["E"]],
    "J": [directions["N"], directions["W"]],
    "7": [directions["S"], directions["W"]],
    "F": [directions["S"], directions["E"]],
    ".": [],
}


def neighbors(lines: list[str], r, c):
    for i, j in tiles[lines[r][c]]:
        nr, nc = r + i, c + j
        if not 0 <= nr < len(lines):
            continue
        if not 0 <= nc < len(lines[nr]):
            continue
        if lines[nr][nc] == ".":
            continue
        yield (nr, nc)


def get_next_tile(lines: list[str], current: tuple[int, int], previous: tuple[int, int]) -> tuple[int, int]:
    for neighbor in neighbors(lines, *current):
        if neighbor == previous:
            continue
        return neighbor
    raise NotImplementedError


def main() -> None:
    lines = read_input(__package__)
    start = next((r, c) for r, line in enumerate(lines) if (c := line.find("S")) >= 0)

    print("start", start)
    # check the input to figure out a possible direction
    tiles["S"] = [directions["N"], directions["E"]]

    current = start
    previous: tuple[int, int] | None = None
    distance = 0
    path = []
    while not distance or current != start:
        path.append(current)
        previous, current = current, get_next_tile(lines, current, previous)
        distance += 1

    assert distance == 13734
    print("Part 1:", distance // 2)


if __name__ == "__main__":
    main()
