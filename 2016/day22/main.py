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
    m = re.match("/dev/grid/node-x(\d+)-y(\d+)"
                 "\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)%", line)
    return (
        int(m.group(1)),
        int(m.group(2)),
        (
            int(m.group(3)),
            int(m.group(4)),
            int(m.group(5)),
            int(m.group(6)),
        )
    )


def is_adjacent(a, b):
    return a[0] == b[0] or a[1] == b[1]


def is_empty(disk):
    return disk[2][1] == 0


def would_fit(a, b):
    return a[2][1] <= b[2][2]


def main():
    lines = readinput(sys.argv[1])
    disks = map(process_line, lines[2:])

    pairs = [
        (a, b)
        for (a, b) in itertools.permutations(disks, 2)
        if not is_empty(a) and would_fit(a, b)
    ]

    print('Part 1: %d' % len(pairs))

if __name__ == "__main__":
    main()
