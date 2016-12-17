import sys
import hashlib
from collections import deque


def gethash(s):
    return hashlib.md5(s).hexdigest()[:4]


def doors(passcode, path):
    return tuple(map(lambda c: c > 'a', gethash(passcode + path)))


def get_moves(passcode, pos, path):
    d = doors(passcode, path)
    (x, y) = pos
    moves = set()
    if d[0] and y > 0:
        moves.add(((x, y - 1), path + 'U'))
    if d[1] and y < 3:
        moves.add(((x, y + 1), path + 'D'))
    if d[2] and x > 0:
        moves.add(((x - 1, y), path + 'L'))
    if d[3] and x < 3:
        moves.add(((x + 1, y), path + 'R'))
    return moves


def main():
    passcode = sys.argv[1]
    paths = []
    queue = deque([((0, 0), '')])
    while queue:
        pos, path = queue.popleft()
        if pos == (3, 3):
            paths.append(path)
            continue
        queue.extend(get_moves(passcode, pos, path))

    print('Part 1: %s' % paths[0])
    print('Part 2: %d' % len(paths[-1]))


if __name__ == "__main__":
    main()
