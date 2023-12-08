from dataclasses import dataclass
from itertools import batched
from typing import Self

from utils.file import read_input


def read_numbers(line: str) -> set[int]:
    return {int("".join(t)) for t in batched(line, n=3)}


@dataclass
class Card:
    card_id: int
    winning_numbers: set[int]
    own_numbers: set[int]
    copies: int = 1

    @classmethod
    def from_line(cls, line: str) -> Self:
        header, body = line.split(":")
        left, right = body.split(" | ", maxsplit=1)
        return cls(
            card_id=int(header[5:]),
            winning_numbers=read_numbers(left),
            own_numbers=read_numbers(right),
        )

    @property
    def number_winning_numbers(self) -> int:
        return len(self.winning_numbers & self.own_numbers)

    @property
    def point_value(self) -> int:
        n = self.number_winning_numbers
        if not n:
            return 0
        return 2 ** (n - 1)


def main() -> None:
    cards: list[Card] = list(map(Card.from_line, read_input(__package__)))
    print("Part 1:", sum(c.point_value for c in cards))

    for card in cards:
        for i in range(card.number_winning_numbers):
            cards[card.card_id + i].copies += 1 * card.copies

    print("Part 2:", sum(c.copies for c in cards))


if __name__ == "__main__":
    main()
