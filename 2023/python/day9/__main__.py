from functools import reduce

from utils.file import read_input


def compute_differences(numbers: list[int]) -> list[int]:
    return [b - a for a, b in zip(numbers, numbers[1:])]


def extrapolate(numbers: list[int], left: bool = False) -> int:
    steps = [numbers]
    while any(n != 0 for n in steps[-1]):
        steps.append(compute_differences(steps[-1]))
    # for i, step in enumerate(steps):
    #    print(" " * i * 2 + "   ".join(map(str,step)))
    if not left:
        return sum(s[-1] for s in steps)

    # a = b -c
    return reduce(lambda c, s: s[0] - c, steps[::-1], 0)


def main() -> None:
    lines = [list(map(int, line.split(" "))) for line in read_input(__package__)]
    print("Part 1:", sum(extrapolate(line) for line in lines))
    print("Part 1:", sum(extrapolate(line, left=True) for line in lines))


if __name__ == "__main__":
    main()
