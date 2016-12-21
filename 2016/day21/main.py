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
    m = re.match('swap position (\d+) with position (\d+)', line)
    if m:
        return ('swap position', tuple([int(i) for i in m.groups()]))

    m = re.match('swap letter (\w) with letter (\w)', line)
    if m:
        return ('swap letter', m.groups())

    m = re.match('rotate (\w+) (\d+) steps?', line)
    if m:
        return ('rotate', (m.group(1), int(m.group(2))))

    m = re.match('rotate based on position of letter (\w)', line)
    if m:
        return ('rotate letter', m.group(1))

    m = re.match('reverse positions (\d+) through (\d+)', line)
    if m:
        return ('reverse', tuple([int(i) for i in m.groups()]))

    m = re.match('move position (\d+) to position (\d+)', line)
    if m:
        return ('move', tuple([int(i) for i in m.groups()]))

    return None


def rotate_right(word, s):
    return word[-s:] + word[:-s]


def rotate_left(word, s):
    return word[s:] + word[:s]


def execute(instruction, word):
    if instruction[0] == 'swap position':
        x, y = instruction[1]
        if x > y:
            x, y = y, x
        word = word[:x] + word[y] + word[x+1:y] + word[x] + word[y+1:]

    elif instruction[0] == 'swap letter':
        x, y = instruction[1]
        import string
        trans = string.maketrans("%s%s" % (x, y), "%s%s" % (y, x))
        word = word.translate(trans)

    elif instruction[0] == 'reverse':
        x, y = instruction[1]
        if x > y:
            x, y = y, x
        word = word[:x] + word[x:y+1][::-1] + word[y+1:]

    elif instruction[0] == 'rotate':
        d, s = instruction[1]
        if d == 'right':
            word = rotate_right(word, s)
        elif d == 'left':
            word = rotate_left(word, s)

    elif instruction[0] == 'move':
        x, y = instruction[1]
        if x < y:
            word = word[:x] + word[x+1:y+1] + word[x] + word[y+1:]
        elif x > y:
            word = word[:y] + word[x] + word[y:x] + word[x+1:]

    elif instruction[0] == 'rotate letter':
        letter = instruction[1]
        index = word.find(letter)
        if index > -1:
            word = rotate_right(word, 1 + index)
        if index >= 4:
            word = rotate_right(word, 1)

    return word


def scramble(instructions, word):
    for instruction in instructions:
        word = execute(instruction, word)
    return word


def unscramble(instructions, word):
    for instruction in instructions[::-1]:
        word = execute(instruction, word, True)
    return word


def main():
    lines = readinput(sys.argv[1])
    instructions = map(process_line, lines)

    r = scramble(instructions, sys.argv[2])
    print('Part 1: %s' % r)

    for p in itertools.permutations(sys.argv[3]):
        p = ''.join(p)
        if scramble(instructions, p) == sys.argv[3]:
            print('Part 2: %s' % p)
            break


if __name__ == "__main__":
    main()
