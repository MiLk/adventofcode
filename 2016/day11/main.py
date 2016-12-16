import sys
import re
import itertools


def readinput(path):
    if not path:
        path = 'input.txt'
    with open(path) as f:
        lines = f.readlines()
    return lines


def build_gm_tuple(g, m):
    return tuple(sorted(g)), tuple(sorted(m))


def process_line(line):
    g = re.findall('a (\w+) generator', line)
    m = re.findall('a (\w+)-compatible microchip', line)
    return build_gm_tuple(g, m)


def generate_move(state):
    level, floors = state
    next_level = []
    if level > 0:
        next_level.append(level - 1)
    if level < 3:
        next_level.append(level + 1)

    combinations = set()
    g, m = floors[level]
    for i in xrange(len(g)):
        combinations.add(build_gm_tuple([g[i]], []))
        for j in xrange(i+1, len(g)):
            combinations.add(build_gm_tuple([g[i], g[i+1+j]], []))
        for j in xrange(len(m)):
            combinations.add(build_gm_tuple([g[i]], [m[j]]))
    for i in xrange(len(m)):
        combinations.add(build_gm_tuple([], [m[i]]))
        for j in xrange(i+1, len(m)):
            combinations.add(build_gm_tuple([], [m[i], m[i+1+j]]))

    moves = itertools.product(next_level, combinations)
    return moves


def remove(floor, move):
    return build_gm_tuple(set(floor[0]) - set(move[0]),
                          set(floor[1]) - set(move[1]))


def add(floor, move):
    return build_gm_tuple(list(floor[0]) + list(move[0]),
                          list(floor[1]) + list(move[1]))


def apply_state(state, move):
    floors = []
    for i, floor in enumerate(state[1]):
        if i == state[0]:
            floors.append(remove(floor, move[1]))
        elif i == move[0]:
            floors.append(add(floor, move[1]))
        else:
            floors.append(floor)
    return (move[0], tuple(floors))


def main():
    lines = readinput(sys.argv[1])
    init = (0, tuple(map(process_line, lines)))
    moves = list(generate_move(init))
    print(init)
    state = apply_state(init, moves[0])
    print(state)

if __name__ == "__main__":
    main()
