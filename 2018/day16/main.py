#!/usr/bin/env python

import itertools
import os
import sys
from collections import defaultdict

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
    result[c] = bool(a > result[b])
    return result


def gtri(registers, a, b, c):
    result = registers[::]
    result[c] = bool(result[a] > b)
    return result


def gtrr(registers, a, b, c):
    result = registers[::]
    result[c] = bool(result[a] > result[b])
    return result


def eqir(registers, a, b, c):
    result = registers[::]
    result[c] = bool(a == result[b])
    return result


def eqri(registers, a, b, c):
    result = registers[::]
    result[c] = bool(result[a] == b)
    return result


def eqrr(registers, a, b, c):
    result = registers[::]
    result[c] = bool(result[a] == result[b])
    return result


OPERATIONS = [
    addr, addi,
    mulr, muli,
    banr, bani,
    borr, bori,
    setr, seti,
    gtir, gtri, gtrr,
    eqir, eqri, eqrr
]


def operations(inst, b, a):
    ops = set()
    for op in OPERATIONS:
        r = tuple(op(list(b), *inst[1:]))
        if r == a:
            ops.add(op)
    return ops


def p1(parsed_input):
    samples, _ = parsed_input
    return sum(len(operations(*s)) >= 3 for s in samples)


def p2(parsed_input):
    samples, program = parsed_input
    opcodes = {opcode: set(OPERATIONS) for opcode in range(16)}
    for s in samples:
        c = s[0][0]
        opcodes[c].intersection_update(operations(*s))

    while True:
        unique_ops = {}
        for op, ops in opcodes.items():
            if len(ops) == 1:
                unique_ops[op] = ops
        for op_, ops_ in unique_ops.items():
            for op, ops in opcodes.items():
                if op != op_:
                    ops.difference_update(ops_)
        if len(unique_ops) == len(opcodes):
            break

    for op in opcodes:
        opcodes[op] = opcodes[op].pop()

    registers = [0, 0, 0, 0]
    for line in program:
        opcode, a, b, c = map(int, line.strip().split(' '))
        registers = opcodes[opcode](registers, a, b, c)
    return registers[0]


def get_input():
    lines = read_input()
    samples = []
    i = 0
    while True:
        if lines[i] in ['', '\n']:
            i += 2
            break
        b = (int(lines[i][9]), int(lines[i][12]), int(lines[i][15]), int(lines[i][18]))
        s = lines[i+1].strip().split(' ')
        inst = (int(s[0]), int(s[1]), int(s[2]), int(s[3]))
        a = (int(lines[i+2][9]), int(lines[i+2][12]), int(lines[i+2][15]), int(lines[i+2][18]))
        samples.append((inst, b, a))
        i += 4
    return samples, lines[i:]


if __name__ == "__main__":
    solve(get_input(), lambda x: x, p1, p2)
