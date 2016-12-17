import sys
import re
import itertools
import hashlib
from collections import deque


def gethash(s):
    return hashlib.md5(s).hexdigest()[:4]

def doors(passcode, path):
    h = gethash(passcode + path)
    return tuple(map(lambda c: c in ['b', 'c', 'd', 'e', 'f'], h))


def get_moves(passcode, pos, path):
    d = doors(passcode, path)
    (x, y) = pos
    moves = set()
    if d[0] and y > 0:
        moves.add('U')
    if d[1] and y < 3:
        moves.add('D')
    if d[2] and x > 0:
        moves.add('L')
    if d[3] and x < 3:
        moves.add('R')
    return moves


def main():
    passcode = sys.argv[1]
    start = (0, 0)
    obj = (3, 3)

    path = ''
    pos = (0, 0)

    paths = []
    queue = deque()
    queue.append((pos, path))
    while queue:
        pos, path = queue.popleft()
        if pos == obj:
            paths.append(path)
            continue
        for move in get_moves(passcode, pos, path):
            np = None
            if move == 'U':
                np = (pos[0], pos[1] - 1)
            elif move == 'D':
                np = (pos[0], pos[1] + 1)
            elif move == 'L':
                np = (pos[0] - 1, pos[1])
            elif move == 'R':
                np = (pos[0] + 1, pos[1])
            queue.append((np, path + move))

    print('Part 1: %s' % paths[0])
    print('Part 2: %d' % len(paths[-1]))


if __name__ == "__main__":
    main()
