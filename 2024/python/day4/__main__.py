from itertools import product

from utils.file import read_input

lines: list[str] = read_input(__package__)


class WordMatcher:
    def __init__(self, words: set[str]) -> None:
        self._words = words
        self._count = 0

    def check(self, word: str) -> None:
        if word in self._words:
            self._count += 1

    @property
    def count(self) -> int:
        return self._count


word_matcher = WordMatcher({"XMAS", "SAMX"})

h, w = len(lines), len(lines[0])
for i, j in product(range(h), range(w)):
    if j < w - 3:
        candidate_right = lines[i][j : j + 4]
        word_matcher.check(lines[i][j : j + 4])

    if i < h - 3:
        candidate_down = "".join(lines[i + k][j] for k in range(4))
        word_matcher.check(candidate_down)

    if i < h - 3 and j < w - 3:
        candidate_down_right = "".join(lines[i + k][j + k] for k in range(4))
        word_matcher.check(candidate_down_right)

    if j >= 3 and i < h - 3:
        candidate_down_left = "".join(lines[i + k][j - k] for k in range(4))
        word_matcher.check(candidate_down_left)

print("Part 1:", word_matcher.count)

count2 = 0
EXPECTED_CORNERS = {"MMSS", "MSSM", "SSMM", "SMMS"}
for i, j in product(range(1, h - 1), range(1, w - 1)):
    if lines[i][j] != "A":
        continue
    corners = "".join([lines[i - 1][j - 1], lines[i - 1][j + 1], lines[i + 1][j + 1], lines[i + 1][j - 1]])
    if corners in EXPECTED_CORNERS:
        count2 += 1

print("Part 1:", count2)
