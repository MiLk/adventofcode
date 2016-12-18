import sys


def readinput(path):
    if not path:
        path = 'input.txt'
    with open(path) as f:
        lines = f.readlines()
    return lines


def get_tile(pos, previous):
    left = previous[pos - 1] if pos > 0 else '.'
    right = previous[pos + 1] if pos < len(previous) - 1 else '.'
    return '^' if left != right else '.'


def main():
    row = readinput(sys.argv[1])[0].strip()
    safes, r = row.count('.'), xrange(0, len(row))
    for i in xrange(1, int(sys.argv[2])):
        row = map(lambda j: get_tile(j, row), r)
        safes += row.count('.')

    print('Safe tiles: %d' % safes)


if __name__ == "__main__":
    main()
