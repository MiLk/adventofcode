from collections.abc import Iterable
from functools import cache
from itertools import groupby

from utils.file import read_input

lines = read_input(__package__)
patterns = {pattern.strip() for pattern in lines[0].split(",")}
patterns_first_letter = {key: set(group) for key, group in groupby(sorted(patterns), lambda x: x[0])}
max_lengths = {key: max(len(pattern) for pattern in patterns) for key, patterns in patterns_first_letter.items()}
designs = lines[1:]


@cache
def is_possible(design: str) -> bool:
    if not design:
        return True
    for i in range(len(design)):
        if design[: i + 1] not in patterns_first_letter.get(design[0], []):
            continue
        if is_possible(design[i + 1 :]):
            return True
    return False


possible_designs = [design for design in designs if is_possible(design)]

# print("Part 1:", len(possible_designs))


@cache
def combinations(design: str) -> int:
    end = max_lengths.get(design[0], 0)
    if not end:
        return 0

    result = 0
    for i in range(end):
        if design[: i + 1] not in patterns_first_letter.get(design[0], []):
            continue
        if i + 1 == len(design):
            return result + 1
        result += combinations(design[i + 1 :])
    return result


print("Part 2:", sum(combinations(d) for d in possible_designs))
