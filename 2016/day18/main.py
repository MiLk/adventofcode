import sys


def readinput(path):
    if not path:
        path = 'input.txt'
    with open(path) as f:
        lines = f.readlines()
    return lines


def get_tile(pos, previous):
    left, center, right = ('.', previous[pos], '.')
    if pos > 0:
        left = previous[pos - 1]
    if pos < len(previous) - 1:
        right = previous[pos + 1]
    traps = [
        ('^', '^', '.'),
        ('.', '^', '^'),
        ('^', '.', '.'),
        ('.', '.', '^'),
    ]
    return '^' if (left, center, right) in traps else '.'


def main():
    row = readinput(sys.argv[1])[0].strip()
    safes, length = row.count('.'), len(row)
    for i in xrange(1, int(sys.argv[2])):
        row = map(lambda j: get_tile(j, row), xrange(0, length))
        safes += row.count('.')

    print('Safe tiles: %d' % safes)


if __name__ == "__main__":
    main()
