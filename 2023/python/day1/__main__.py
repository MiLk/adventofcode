import asyncio
import re
from operator import itemgetter
from typing import Sequence

from utils.file import read_input

DIGITS_RE = re.compile(r"(\d)")

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


def find_digit(line: str) -> tuple[int, int]:
    first = min(
        (
            (word, pos)
            for word in WORDS.keys() | WORDS.values()
            if (pos := line.find(str(word))) > -1
        ),
        key=itemgetter(1),
    )[0]
    second = max(
        (
            (word, pos)
            for word in WORDS.keys() | WORDS.values()
            if (pos := line.rfind(str(word))) > -1
        ),
        key=itemgetter(1),
    )[0]

    return (
        first if isinstance(first, int) else WORDS[first],
        second if isinstance(second, int) else WORDS[second],
    )


def concat_first_last_digits(t: Sequence[int]) -> int:
    return int(f"{t[0]}{t[-1]}")


async def main():
    lines = read_input()

    digits = (DIGITS_RE.findall(line) for line in lines)
    print("Part 1:", sum(concat_first_last_digits(d) for d in digits))

    digits = (find_digit(line) for line in lines)
    print("Part 2:", sum(concat_first_last_digits(d) for d in digits))


if __name__ == "__main__":
    asyncio.run(main())
