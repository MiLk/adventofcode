import re
from collections import Counter
from math import prod

from utils.file import read_input

LINE_RE = re.compile(r"^p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)$")


def parse_line(line: str) -> tuple[complex, complex]:
    m = LINE_RE.match(line)
    assert m is not None
    return complex(int(m.group(1)), int(m.group(2))), complex(int(m.group(3)), int(m.group(4)))


robots = list(map(parse_line, read_input(__package__)))
w, h = (101, 103) if len(robots) > 20 else (11, 7)


def move_robot(robot: tuple[complex, complex]) -> tuple[complex, complex]:
    position, velocity = robot
    new_position = position + velocity
    x, y = new_position.real, new_position.imag
    return complex(int(x % w), int(y % h)), velocity


def move_robots(robots_: list[tuple[complex, complex]]) -> list[tuple[complex, complex]]:
    return [move_robot(robot) for robot in robots_]


def count_quadrants(robots_: list[tuple[complex, complex]]) -> list[int]:
    c = Counter(p for p, _ in robots_)
    quadrants = [0, 0, 0, 0]
    wm, hm = (w - 1) / 2, (h - 1) / 2
    for tile, count in c.items():
        if tile.real == wm or tile.imag == hm:
            continue
        qn = 0
        if tile.real > wm:
            qn += 1
        if tile.imag > hm:
            qn += 2
        quadrants[qn] += count
    return quadrants


for i in range(100):
    robots = move_robots(robots)

security_factor = prod(count_quadrants(robots))
print("Part 1:", security_factor)

for i in range(1_000_000):
    robots = move_robots(robots)
    qs = count_quadrants(robots)
    new_security_factor = prod(qs)
    if i > 8000 and new_security_factor < security_factor:
        positions = {p for p, _ in robots}
        for y in range(h):
            for x in range(w):
                print("#" if (x + y * 1j) in positions else ".", end="")
            print("")
        print("Part2:", i + 101)
    security_factor = min(security_factor, new_security_factor)
