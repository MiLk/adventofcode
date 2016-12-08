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
        (arg0, arg1, arg3, arg4, shift) = line.split(' ')
        (arg3label, index) = arg3.split('=')
        index = int(index)
        shift = int(shift)
        if arg1 == 'row':
            tmp = list(screen[index])
            for i in xrange(0, 50):
                screen[index][i] = tmp[(i-shift+50) % 50]
        elif arg1 == 'column':
            tmp = [list(screen[i]) for i in xrange(0, 6)]
            for i in xrange(0, 6):
                old = (i-shift+6) % 6
                screen[i][index] = tmp[old][index]

    return screen


def main():
    lines = readinput(sys.argv[1])

    screen = [[' '] * 50 for i in range(0, 6)]

    for line in lines:
        screen = process_line(screen, line.strip())

    c = 0
    for i in xrange(0, 6):
        for j in xrange(0, 50):
            if screen[i][j] == '#':
                c += 1

    print('Step 1: %d' % c)

    print('Step 2:')
    for i in xrange(0, len(screen)):
        print(''.join(screen[i]))


if __name__ == "__main__":
    main()
