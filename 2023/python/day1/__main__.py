import asyncio
import re
from typing import Sequence

from utils.file import read_input

PART1_DIGITS_RE = re.compile(r"(\d)")
# https://stackoverflow.com/a/5616910
PART2_DIGITS_RE = re.compile(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))")

WORDS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def str_to_digit(s: str) -> str:
    if s.isdigit():
        return s
    return str(WORDS[s])


def concat_first_last_digits(t: Sequence[str]) -> int:
    return int("".join(map(str_to_digit, (t[0], t[-1]))))


def solve(pattern: re.Pattern[str], lines: Sequence[str]) -> int:
    return sum(concat_first_last_digits(d) for d in (pattern.findall(line) for line in lines))


async def main() -> None:
    lines = read_input(__package__)

    print("Part 1:", solve(PART1_DIGITS_RE, lines))
    print("Part 2:", solve(PART2_DIGITS_RE, lines))


if __name__ == "__main__":
    asyncio.run(main())
