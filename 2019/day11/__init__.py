from collections import defaultdict
from typing import Dict, Tuple

from intcode import Computer
from utils import int_list_lines

parse_input = int_list_lines(',')

directions: Dict[int, Tuple[int, int]] = {
    0: (0, 1),   # UP
    1: (1, 0),   # RIGHT
    2: (0, -1),  # DOWN
    3: (-1, 0),  # LEFT
}


def p1(lines):
    # All of the panels are currently black
    panels = defaultdict(int)
    painted = set()
    pos = ((0, 0), 0)

    def fetch():
        while True:
            # provide 0 if the robot is over a black panel
            # or 1 if the robot is over a white panel
            yield panels[pos[0]]

    computer = Computer(lines[0])
    computer.input = fetch()
    runnable = computer.run_output()

    try:
        while True:
            panels[pos[0]] = next(runnable)
            painted.add(pos[0])
            turn = next(runnable)
            d = (pos[1] + (3 if turn == 0 else 1)) % 4
            pos = ((pos[0][0] + directions[d][0], pos[0][1] + directions[d][1]), d)
    except StopIteration:
        pass

    return len(painted)


def p2(lines):
    # The rest of the panels are still black,
    # but it looks like the robot was expecting to start on a white panel, not a black one.
    panels = defaultdict(int)
    panels[(0, 0)] = 1
    pos = ((0, 0), 0)

    def fetch():
        while True:
            # provide 0 if the robot is over a black panel
            # or 1 if the robot is over a white panel
            yield panels[pos[0]]

    computer = Computer(lines[0])
    computer.input = fetch()
    runnable = computer.run_output()

    try:
        while True:
            panels[pos[0]] = next(runnable)
            turn = next(runnable)
            d = (pos[1] + (3 if turn == 0 else 1)) % 4
            pos = ((pos[0][0] + directions[d][0], pos[0][1] + directions[d][1]), d)
    except StopIteration:
        pass

    xs = sorted(x for x, _ in panels.keys())
    ys = sorted(y for _, y in panels.keys())
    minx, maxx, miny, maxy = min(xs), max(xs), min(ys), max(ys)

    return '\n' + '\n'.join([
        ''.join(['█' if panels[(x, y)] == 1 else ' ' for x in range(minx, maxx + 1)])
        for y in range(maxy, miny - 1, -1)
    ])
