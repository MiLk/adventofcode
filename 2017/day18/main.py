#!/usr/bin/env python

from __future__ import print_function
from __future__ import unicode_literals


import os
import sys


def read_input(path):
    if not path:
        path = 'input.txt'
    with open(path) as f:
        lines = f.readlines()
    return lines


def process_line(line):
    return line.strip().split(' ')


def p1(lines):
    regs = dict()
    last_sound = None

    def get_value(x):
        if len(x) == 1 and ord('a') <= ord(x) <= ord('z'):
            return regs.get(x, 0)
        return int(x)

    ip = 0

    while 0 <= ip < len(lines):
        l = lines[ip]
        if l[0] == 'snd':
            last_sound = get_value(l[1])
        elif l[0] == 'set':
            regs[l[1]] = get_value(l[2])
        elif l[0] == 'add':
            regs[l[1]] = get_value(l[1]) + get_value(l[2])
        elif l[0] == 'mul':
            regs[l[1]] = get_value(l[1]) * get_value(l[2])
        elif l[0] == 'mod':
            regs[l[1]] = get_value(l[1]) % get_value(l[2])
        elif l[0] == 'rcv':
            if get_value(l[1]) != 0:
                return last_sound
        elif l[0] == 'jgz':
            if get_value(l[1]) > 0:
                ip += get_value(l[2])
                continue
        ip += 1

    return None


def p2(lines, pid, r, w):
    regs = {'p': pid}

    r = os.fdopen(r)

    def get_value(x):
        if len(x) == 1 and ord('a') <= ord(x) <= ord('z'):
            return regs.get(x, 0)
        return int(x)

    ip = 0
    c = 0

    while 0 <= ip < len(lines):
        l = lines[ip]
        if l[0] == 'snd':
            if pid == 1:
                c += 1
                print("Send", c)
            os.write(w, "%d\n" % get_value(l[1]))
        elif l[0] == 'set':
            regs[l[1]] = get_value(l[2])
        elif l[0] == 'add':
            regs[l[1]] = get_value(l[1]) + get_value(l[2])
        elif l[0] == 'mul':
            regs[l[1]] = get_value(l[1]) * get_value(l[2])
        elif l[0] == 'mod':
            regs[l[1]] = get_value(l[1]) % get_value(l[2])
        elif l[0] == 'rcv':
            v = r.readline()
            regs[l[1]] = int(v.strip())
        elif l[0] == 'jgz':
            if get_value(l[1]) > 0:
                ip += get_value(l[2])
                continue
        ip += 1

    return None


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else None
    lines = read_input(path)
    lines = list(map(process_line, lines))

    s1 = p1(lines)
    print('Part 1:', s1)

    r1, w1 = os.pipe()
    r2, w2 = os.pipe()

    pid = os.fork()
    if pid:          # Parent
        os.close(w1)
        os.close(r2)
        p2(lines, 0, r1, w2)
    else:           # Child
        os.close(w2)
        os.close(r1)
        p2(lines, 1, r2, w1)


if __name__ == "__main__":
    main()
