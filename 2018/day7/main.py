#!/usr/bin/env python

import os
import sys
from collections import defaultdict

sys.path.insert(0, os.path.abspath('../..'))

from utils import solve # nopep8


def process_line(line):
    s = line.strip().split(' ')
    return s[1], s[7]


def resolve_dependencies(lines):
    steps = set()
    blockers = defaultdict(set)
    for a, b in lines:
        steps.add(a)
        steps.add(b)
        blockers[b] |= {a}
    return steps, blockers


def p1(lines):
    steps, blockers = resolve_dependencies(lines)

    order = list()
    while len(order) != len(steps):
        for s in sorted(steps):
            if s in order:
                continue
            if len(blockers[s] - set(order)) == 0:
                order.append(s)
                break

    return ''.join(order)


def find_free_worker(workers):
    for wid, task in workers.items():
        if task[0] is None:
            return wid
    return None


def p2(lines):
    steps, blockers = resolve_dependencies(lines)

    workers = {0: (None, 0), 1: (None, 0), 2: (None, 0), 3: (None, 0), 4: (None, 0)}
    done = set()
    processed = set()
    t = 0
    while len(done) != len(steps):
        for wid, task in workers.items():
            if task[1] <= t and task[0] is not None:
                done.add(task[0])
                workers[wid] = (None, 0)

        for s in sorted(steps):
            # Skip finished and in progress steps
            if s in processed:
                continue
            # Skip not read steps
            if len(blockers[s] - set(done)) > 0:
                continue

            wid = find_free_worker(workers)
            # No worker available
            if wid is None:
                continue

            workers[wid] = (s, t + 61 + ord(s) - ord('A'))
            processed.add(s)
            t -= 1
            break
        t += 1

    return t - 1


if __name__ == "__main__":
    solve(sys.argv, process_line, p1, p2)
