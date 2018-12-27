#!/usr/bin/env python

import itertools
import os
import sys
from collections import defaultdict
import re
import math
import copy

sys.path.insert(0, os.path.abspath('../..'))

from utils import solve, read_input  # nopep8


boost = 0

class Group:
    id = n = hp = ap = init = 0
    type = atype = w = i = None
    target = None

    def __init__(self, type, id, n, hp, ap, atype, init, i, w):
        self.type = type
        self.id = id
        self.n = n
        self.hp = hp
        self.ap = ap
        self.atype = atype
        self.init = init
        self.i = i
        self.w = w

    def __str__(self):
        return f"{type_str[self.type]} {self.id} {self.n}x"

    def effective_power(self):
        if self.n == 0:
            return 0
        if self.type == IMMUNE_SYSTEM:
            return self.n * (self.ap + boost)
        return self.n * self.ap

    def choose_target(self, targets, chosen):
        enemy = sorted([
            t for t in targets
            if t not in chosen and t.type != self.type and t.n > 0
        ], key=lambda t: (-self.damage(t), -t.effective_power()))
        if not enemy or self.damage(enemy[0]) == 0:
            self.target = None
        else:
            self.target = enemy[0]
        return self.target

    def damage(self, group):
        if group.i and self.atype in group.i:
            return 0
        d = self.effective_power()
        if group.w and self.atype in group.w:
            return 2 * d
        return d

    def attack(self):
        d = self.damage(self.target)
        kill = min(math.floor(d / self.target.hp), self.target.n)
        #print(f'{self} attacks {self.target} dealing {d} damages, killing {kill} units')
        self.target.n -= kill


def p1(groups_src):
    return None
    groups = copy.deepcopy(groups_src)
    while True:
        # target selection
        chosen = set()
        for g in sorted(groups, key=lambda g: (-g.effective_power(), -g.init)):
            if g.n <= 0:
                continue
            t = g.choose_target(groups, chosen)
            chosen.add(t)

        # attack
        for g in sorted(groups, key=lambda g: -g.init):
            if g.n <= 0:
                continue
            if not g.target:
                continue
            g.attack()

        for g in groups:
            if g.n > 0:
                print(str(g))
        print()

        if sum(g.n > 0 for g in groups if g.type == IMMUNE_SYSTEM) == 0:
            return sum(g.n for g in groups if g.type == INFECTION)
        if sum(g.n > 0 for g in groups if g.type == INFECTION) == 0:
            return sum(g.n for g in groups if g.type == IMMUNE_SYSTEM)


def p2(groups_src):
    global boost

    boost = 59
    while True:
        groups = copy.deepcopy(groups_src)
        boost += 1
        print(f"Trying with boost: {boost}")
        while True:
            # target selection
            chosen = set()
            for g in sorted(groups, key=lambda g: (-g.effective_power(), -g.init)):
                if g.n <= 0:
                    continue
                t = g.choose_target(groups, chosen)
                chosen.add(t)

            # attack
            for g in sorted(groups, key=lambda g: -g.init):
                if g.n <= 0:
                    continue
                if not g.target:
                    continue
                g.attack()

            if sum(g.n > 0 for g in groups if g.type == IMMUNE_SYSTEM) == 0:
                for g in groups:
                    if g.n > 0:
                        print(str(g))
                print()
                break
            if sum(g.n > 0 for g in groups if g.type == INFECTION) == 0:
                for g in groups:
                    if g.n > 0:
                        print(str(g))
                print()
                return sum(g.n for g in groups if g.type == IMMUNE_SYSTEM)


def get_immune_weakness(s):
    if not s:
        return None, None

    w = None
    i = None
    for p in s.split(';'):
        if p.strip().startswith('weak'):
            w = [
                x.strip(',') for x in p.strip().split(' ')[2:]
            ]
        if p.strip().startswith('immune'):
            i = [
                x.strip(',') for x in p.strip().split(' ')[2:]
            ]
    return i, w


def process_line(id, line, type):
    m = re.match(r'^(\d+) units each with (\d+) hit points (?:\((.+)\) )?with an attack that does (\d+) ([^\s]+) damage at initiative (\d+)\s*$', line)
    i, w = get_immune_weakness(m.group(3))

    return Group(
        type,
        id,
        int(m.group(1)),
        int(m.group(2)),
        int(m.group(4)),
        m.group(5),
        int(m.group(6)),
        i,
        w
    )

IMMUNE_SYSTEM = 0
INFECTION = 1
type_str = {
    0: 'Immune system',
    1: 'Infection',
}

def get_input():
    lines = read_input()
    return [
        process_line(i+1, lines[1+i], IMMUNE_SYSTEM) for i in range(10)
    ] + [
        process_line(i+1, lines[13+i], INFECTION) for i in range(10)
    ]


if __name__ == "__main__":
    solve(get_input(), lambda x: x, p1, p2)
