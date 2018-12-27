#!/usr/bin/env python

import os
import sys

sys.path.insert(0, os.path.abspath('../..'))

from utils import solve, read_input  # nopep8


def addr(registers, a, b, c):
    result = registers[::]
    result[c] = result[a] + result[b]
    return result


def addi(registers, a, b, c):
    result = registers[::]
    result[c] = result[a] + b
    return result


def mulr(registers, a, b, c):
    result = registers[::]
    result[c] = result[a] * result[b]
    return result


def muli(registers, a, b, c):
    result = registers[::]
    result[c] = result[a] * b
    return result


def banr(registers, a, b, c):
    result = registers[::]
    result[c] = result[a] & result[b]
    return result


def bani(registers, a, b, c):
    result = registers[::]
    result[c] = result[a] & b
    return result


def borr(registers, a, b, c):
    result = registers[::]
    result[c] = result[a] | result[b]
    return result


def bori(registers, a, b, c):
    result = registers[::]
    result[c] = result[a] | b
    return result


def setr(registers, a, b, c):
    result = registers[::]
    result[c] = result[a]
    return result


def seti(registers, a, b, c):
    result = registers[::]
    result[c] = a
    return result


def gtir(registers, a, b, c):
    result = registers[::]
    result[c] = int(a > result[b])
    return result


def gtri(registers, a, b, c):
    result = registers[::]
    result[c] = int(result[a] > b)
    return result


def gtrr(registers, a, b, c):
    result = registers[::]
    result[c] = int(result[a] > result[b])
    return result


def eqir(registers, a, b, c):
    result = registers[::]
    result[c] = int(a == result[b])
    return result


def eqri(registers, a, b, c):
    result = registers[::]
    result[c] = int(result[a] == b)
    return result


def eqrr(registers, a, b, c):
    result = registers[::]
    result[c] = int(result[a] == result[b])
    return result


def p1(lines):
    ip, program = lines
    r = [0 for _ in range(6)]
    while True:
        if r[ip] >= len(program):
            print('Invalid IP')
            return r[0]
        r = globals()[program[r[ip]][0]](r, *program[r[ip]][1:])
        r[ip] += 1


def p2(lines):
    ip, program = lines
    r = [0 for _ in range(6)]
    r[0] = 1
    while True:
        if r[ip] >= len(program):
            return r[0]

        if r[ip] == 1:
            # r0: sum of factors of r2
            # r1: tmp
            # r2: input
            # r3: outer counter
            # r4: IP
            # r5: inner counter
            print(r)
            # for r3 in range(1, r[2] + 1):
            #     for r5 in range(1, r[2] + 1):
            #         if r3 * r5 == r[2]:
            #             r[0] += r3
            for r3 in range(1, r[2] + 1):
                if r[2] % r3 == 0:
                    r[0] += r3
            return r[0]

        r = globals()[program[r[ip]][0]](r, *program[r[ip]][1:])
        r[ip] += 1


def process_line(line):
    if not line.strip() or line.strip().startswith('#'):
        return None
    s = line.strip().split(' ')
    return s[0], int(s[1]), int(s[2]), int(s[3])


def get_input():
    lines = read_input()
    return int(lines[0][4]), [l for l in map(process_line, lines[1:]) if l]


if __name__ == "__main__":
    solve(get_input(), lambda x: x, p1, p2)
