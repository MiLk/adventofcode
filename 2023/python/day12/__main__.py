from functools import cache

from utils.file import read_input


@cache
def count_matching_arrangement(springs: str, groups: tuple[int, ...]) -> int:
    if len(groups) == 0:
        return int("#" not in springs)

    largest_group = max(groups)
    largest_idx = groups.index(largest_group)
    lg, rg = groups[:largest_idx], groups[largest_idx + 1 :]

    # space required to fit the left groups
    previous_springs = sum(lg) + len(lg)
    # space required to fit the right groups
    following_springs = sum(rg) + len(rg)

    total = 0
    # we exclude the space required to fit the left and right groups
    # and we try to check if the largest group could fit in the remaining space
    for i in range(previous_springs, len(springs) - following_springs - largest_group + 1):
        block_springs = springs[i : i + largest_group]
        left_side = "" if i == 0 else springs[i - 1]
        right_side = "" if i + largest_group == len(springs) else springs[i + largest_group]

        # we check that the whole block could be filled with damaged springs, but has no damaged springs around
        if "." not in block_springs and left_side != "#" and right_side != "#":
            left_total = count_matching_arrangement(springs[: i - len(left_side)], lg)
            right_total = count_matching_arrangement(springs[i + largest_group + len(right_side) :], rg)
            total += left_total * right_total
    return total


def solve(records: list[tuple[str, tuple[int, ...]]]) -> int:
    return sum(count_matching_arrangement(spring, groups) for spring, groups in records)


def main() -> None:
    records: list[tuple[str, tuple[int, ...]]] = [
        (springs, tuple(map(int, groups.split(","))))
        for springs, groups in (line.split(" ", maxsplit=1) for line in read_input(__package__))
    ]
    print("Part 1:", solve(records))
    unfolded = [
        (
            "?".join(
                [
                    springs,
                ]
                * 5
            ),
            groups * 5,
        )
        for springs, groups in records
    ]
    print("Part 2:", solve(unfolded))


if __name__ == "__main__":
    main()
