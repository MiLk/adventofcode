import re
from collections.abc import Iterable

from utils.file import read_input


def parse_line(line) -> tuple[int, list[int]]:
    value, numbers = line.split(":", maxsplit=2)
    return int(value.strip()), [int(n) for n in numbers.strip().split(" ")]


def compute(numbers: list[int]) -> Iterable[int]:
    if len(numbers) == 1:
        yield numbers[0]
        return
    heads, tail = numbers[:-1], numbers[-1]
    for computed in compute(heads):
        yield computed + tail
        yield computed * tail


def is_solvable(value: int, numbers: list[int]) -> bool:
    return any(n == value for n in compute(numbers))


equations = list(map(parse_line, read_input(__package__)))

print("Part 1:", sum(value for value, numbers in equations if is_solvable(value, numbers)))


def fill_operators(numbers: list[int]) -> Iterable[list[tuple[int, str]]]:
    if len(numbers) == 1:
        yield [(numbers[0], "")]
        return
    head, tail = numbers[0], numbers[1:]
    for filled in list(fill_operators(tail)):
        yield [(head, "+")] + filled
        yield [(head, "*")] + filled
        yield [(head, "||")] + filled


def evaluate(expression: list[tuple[int, str]]) -> int:
    if len(expression) == 1:
        return expression[0][0]
    (first, operator), (second, remaining_op), tail = expression[0], expression[1], expression[2:]
    match operator:
        case "+":
            return evaluate([(first + second, remaining_op)] + tail)
        case "*":
            return evaluate([(first * second, remaining_op)] + tail)
        case "||":
            return evaluate([(int(f"{first}{second}"), remaining_op)] + tail)
        case _:
            raise NotImplementedError


def is_solvable_concat(value: int, numbers: list[int]) -> bool:
    return any(evaluate(expr) == value for expr in fill_operators(numbers))


print("Part 2:", sum(value for value, numbers in equations if is_solvable_concat(value, numbers)))
