#!/usr/bin/env python

import os
import sys
from collections import defaultdict, Counter

sys.path.insert(0, os.path.abspath('../..'))

from utils import solve  # nopep8


def get_entries(lines):
    entries = sorted(lines, key=lambda l: l[0])
    state = '.'
    guard_id = 0
    last = None

    m = defaultdict(dict)

    for date, msg in entries:
        if msg[0] == 'G':
            guard_id = int(msg.split(' ')[1][1:])
            state = '.'
            last = date
            continue

        start = last[1][1] if last and last[1][0] == 0 else 0
        end = date[1][1]

        # print(date[0], guard_id, start, end, state, date, msg)

        for i in range(start, end):
            m[(date[0], guard_id)][i] = state

        if msg == 'falls asleep':
            state = '#'
        elif msg == 'wakes up':
            state = '.'
        else:
            print(msg, file=sys.stderr)
            raise Exception('Unknown message')
        last = date
    return m


def p1(lines):
    m = get_entries(lines)

    counter = defaultdict(int)
    for (date, gid), st in m.items():
        counter[gid] += sum(c == '#' for c in st.values())
    c = Counter(counter)
    most_sleeping = c.most_common(1)[0][0]

    minutes_counter_dict = defaultdict(int)
    for (date, gid), st in m.items():
        if gid != most_sleeping:
            continue
        for k, v in st.items():
            if v == '#':
                minutes_counter_dict[k] += 1
    mc = Counter(minutes_counter_dict)
    most_sleeped = mc.most_common(1)[0][0]

    return most_sleeping * most_sleeped


def p2(lines):
    m = get_entries(lines)

    minutes_counter_dict = defaultdict(int)
    for (date, gid), st in m.items():
        for k, v in st.items():
            if v == '#':
                minutes_counter_dict[(gid, k)] += 1
    mc = Counter(minutes_counter_dict)
    r = mc.most_common(1)[0][0]

    return r[0] * r[1]


def process_line(line):
    sp = line.strip().split(' ')
    day = sp[0].strip('[').split('-')
    hour = sp[1].strip(']').split(':')
    return ((int(day[0]), int(day[1]), int(day[2])), (int(hour[0]), int(hour[1]))), ' '.join(sp[2:])


if __name__ == "__main__":
    solve(sys.argv, process_line, p1, p2)
