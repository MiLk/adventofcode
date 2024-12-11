from collections import Counter, defaultdict
from functools import cache

from utils.file import int_list_line, read_input


@cache
def blink_one(stone: int) -> list[int]:
    if stone == 0:
        return [1]

    length = len(str(stone))
    if length % 2 == 0:
        mid = length // 2
        return [stone // 10**mid, stone % 10**mid]
    return [stone * 2024]


def p1() -> int:
    stones = int_list_line(read_input(__package__)[0], " ")
    for _ in range(25):
        stones = [result for stone in stones for result in blink_one(stone)]
    return len(stones)


print("Part 1:", p1())


# Keeping a list was a bad idea due to the amount of memory allocations required
def p2():
    def blink(stones_: defaultdict[int, int]) -> defaultdict[int, int]:
        new_stones: defaultdict[int, int] = defaultdict(int)
        for stone, count in stones_.items():
            for new_stone in blink_one(stone):
                new_stones[new_stone] += count
        return new_stones

    stones = defaultdict(int, Counter(int_list_line(read_input(__package__)[0], " ")))
    for _ in range(75):
        stones = blink(stones)

    return sum(stones.values())


print("Part 2:", p2())
