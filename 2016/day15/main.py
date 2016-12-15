import sys
import re
import itertools


def readinput(path):
    if not path:
        path = 'input.txt'
    with open(path) as f:
        lines = f.readlines()
    return lines


def process_line(line):
    m = re.match(r'Disc #(\d+) has (\d+) positions;'
                 ' at time=0, it is at position (\d+)', line)
    (a, b, c) = m.groups()
    return (int(a), int(b), int(c))


def is_aligned(t, discs):
    for (slot, positions, start) in discs:
        ticks = t + slot
        pos = (ticks + start) % positions
        if pos != 0:
            return False

    return True


def main():
    lines = readinput(sys.argv[1])
    discs = map(process_line, lines)

    for i in itertools.count():
        if is_aligned(i, discs):
            print('Step 1: %d' % i)
            break

    discs.append((len(discs) + 1, 11, 0))
    for i in itertools.count():
        if is_aligned(i, discs):
            print('Step 2: %d' % i)
            break


if __name__ == "__main__":
    main()
