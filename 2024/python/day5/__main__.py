from collections.abc import Iterable
from math import floor

from black.trans import defaultdict
from more_itertools.recipes import partition

from utils.file import read_input

lines = read_input(__package__)

rules: list[tuple[int, int]] = []
updates: list[list[int]] = []
for line in lines:
    if line[2] == "|":
        rules.append((int(line[:2]), int(line[3:])))
    elif "," in line:
        updates.append(list(map(int, line.split(","))))

rules_after = defaultdict(set)
rules_before = defaultdict(set)
for rule in rules:
    rules_after[rule[0]].add(rule[1])
    rules_before[rule[1]].add(rule[0])


def check_rule(page: int, before: list[int], after: list[int]) -> bool:
    return all(p not in rules_after[page] for p in before) and all(p not in rules_before[page] for p in after)


def is_ordered(pages: list[int]) -> bool:
    return all(check_rule(pages[i], pages[:i], pages[i + 1 :]) for i in range(len(pages)))


def middle_pages(updates_: Iterable[list[int]]) -> Iterable[int]:
    return (update[floor((len(update) - 1) / 2)] for update in updates_)


unordered, ordered = partition(is_ordered, updates)
print("Part 1", sum(middle_pages(ordered)))


def reorder(pages_: list[int]):
    pages = pages_[:]  # Copy before mutations
    while not is_ordered(pages):  # Pray for no infinite loop
        for i in range(len(pages)):
            page = pages[i]
            before, after = pages[:i], pages[i + 1 :]
            rule_before, rule_after = rules_before[page], rules_after[page]

            move_before = next((p for p in before if p in rule_after), None)
            if move_before:
                pages = pages[:i] + pages[i + 1 :]
                idx = pages.index(move_before)
                pages.insert(idx, page)
                break
            move_after = next((p for p in after if p in rule_before), None)
            if move_after:
                pages = pages[:i] + pages[i + 1 :]
                idx = -pages[::-1].index(move_after)
                if idx == 0:
                    pages.append(page)
                else:
                    pages.insert(idx, page)
    return pages


reordered = list(map(reorder, unordered))
print("Part 2", sum(middle_pages(reordered)))
