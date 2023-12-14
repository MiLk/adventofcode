from itertools import takewhile

from utils.file import read_input


def inverse(lines: list[str]) -> list[str]:
    height = len(lines)
    width = len(lines[0])
    return ["".join(lines[r][c] for r in range(height)) for c in range(width)]


def tilt(line: str, opposite: bool = False) -> str:
    line = line[::-1] if opposite else line
    new_line = ""
    cubes = [i for i, c in enumerate(line) if c == "#"]
    for cube in cubes:
        rounds, empty = line[len(new_line) : cube].count("O"), line[len(new_line) : cube].count(".")
        new_line += "O" * rounds + "." * empty + "#"
    rounds, empty = line[len(new_line) :].count("O"), line[len(new_line) :].count(".")
    new_line += "O" * rounds + "." * empty
    return new_line[::-1] if opposite else new_line


def cycle(lines: list[str]) -> list[str]:
    tilted_north = [tilt(line) for line in inverse(lines)]
    tilted_west = [tilt(line) for line in inverse(tilted_north)]
    tilted_south = [tilt(line, True) for line in inverse(tilted_west)]
    tilted_east = [tilt(line, True) for line in inverse(tilted_south)]
    return tilted_east


def compute_load(lines: list[str]) -> int:
    height = len(lines)
    return sum(sum(height - i for i, c in enumerate(line) if c == "O") for line in lines)


def main() -> None:
    lines = read_input(__package__)

    tilted = [tilt(line) for line in inverse(lines)]

    print("Part 1:", compute_load(tilted))

    pattern = [
        93720,
        93740,
        93730,
        93731,
        93738,
        93746,
        93751,
        93743,
        93728,
        93730,
        93731,
        93735,
        93736,
        93724,
        93713,
        93725,
        93718,
        93701,
        93698,
        93694,
        93688,
        93683,
        93684,
        93688,
        93678,
        93686,
    ]

    # visited = []
    for i in range(1, 270):
        lines = cycle(lines)
        if i > 150:
            load = compute_load(inverse(lines))

            # We first try to find a cycle
            # visited.append(load)
            # if load in visited:
            #    print("Cycle found at", i, "with load of", load)

            # Looking at what is printed, there is a cycle of 26 iterations after ~150 iterations
            # Let's look at the iterations before 260 to find the patten easily
            # if len(visited) > 26:
            #    print(i, load, visited[-26:])
            assert pattern[i % 26] == load, f"Pattern mismatch at {i} with load of {load} - expected: {pattern[i%26]}"

    print("Part 2:", pattern[1000000000 % 26])
    # 93751 too high


if __name__ == "__main__":
    main()
