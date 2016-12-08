import sys


def readinput(path):
    if not path:
        path = 'input.txt'
    with open(path) as f:
        lines = f.readlines()
    return lines


def process_line(screen, line):
    instruction = line[:line.find(' ')]
    if instruction == 'rect':
        args = line[5:]
        (a, b) = args.split('x')
        for i in xrange(0, int(b)):
            for j in xrange(0, int(a)):
                screen[i][j] = '#'
    elif instruction == 'rotate':
        (_, arg1, arg3, _, shift) = line.split(' ')
        (_, index) = arg3.split('=')
        index = int(index)
        shift = int(shift)
        if arg1 == 'row':
            tmp = list(screen[index])
            for i in xrange(0, 50):
                screen[index][i] = tmp[(i-shift+50) % 50]
        elif arg1 == 'column':
            tmp = [list(screen[i]) for i in xrange(0, 6)]
            for i in xrange(0, 6):
                screen[i][index] = tmp[(i-shift+6) % 6][index]

    return screen


def main():
    lines = readinput(sys.argv[1])

    screen = [list(x) for x in [[' '] * 50] * 6]

    for line in lines:
        screen = process_line(screen, line.strip())

    c = reduce(lambda acc, line: acc + line.count('#'), screen, 0)
    print('Step 1: %d' % c)

    print('Step 2:')
    for i in xrange(0, len(screen)):
        print(''.join(screen[i]))


if __name__ == "__main__":
    main()
