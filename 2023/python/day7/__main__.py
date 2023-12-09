from collections import Counter
from dataclasses import dataclass
from functools import cached_property

from utils.file import read_input

CARD_STRENGTHS_P1: dict[str, int] = {
    card: 14 - i for i, card in enumerate(["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"])
}

CARD_STRENGTHS_P2: dict[str, int] = {
    card: 13 - i for i, card in enumerate(["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"])
}


@dataclass
class Hand:
    cards: str
    bid: int

    def __init__(self, cards: str, bid: str) -> None:
        self.cards = cards
        self.bid = int(bid)

    def hand_type(self, p2: bool = False) -> int:
        joker = 0
        c = Counter(self.cards).most_common(5)

        if p2:
            joker = next((t[1] for t in c if t[0] == "J"), 0)
            c = [t for t in c if t[0] != "J"]

        first = c[0][1] if c else 0
        second = c[1][1] if len(c) > 1 else 0

        # Five of a kind
        if first + joker == 5:
            return 6
        # Four of a kind
        if first + joker == 4:
            return 5
        # Full house
        if first + joker == 3 and second == 2:
            return 4
        # Three of a kind
        if first + joker == 3:
            return 3
        # Two pairs
        if first + joker == 2 and second == 2:
            return 2
        # One pair
        if first + joker == 2:
            return 1
        # High card
        return 0


def main() -> None:
    hands = [Hand(*line.split(" ", maxsplit=1)) for line in read_input(__package__)]
    sorted_hands = sorted(
        hands,
        key=lambda h: (h.hand_type(), tuple(CARD_STRENGTHS_P1[c] for c in h.cards)),
    )
    print("Part 1:", sum(hand.bid * rank for rank, hand in enumerate(sorted_hands, start=1)))

    sorted_hands_p2 = sorted(
        hands,
        key=lambda h: (h.hand_type(True), tuple(CARD_STRENGTHS_P2[c] for c in h.cards)),
    )
    print("Part 2:", sum(hand.bid * rank for rank, hand in enumerate(sorted_hands_p2, start=1)))


if __name__ == "__main__":
    main()
