import sys


def readinput(path):
    if not path:
        path = 'input.txt'
    with open(path) as f:
        lines = f.readlines()
    return lines


def process_char_1(char, pos):
    if char == 'L' and (pos % 3) != 1:
        pos -= 1
    elif char == 'R' and (pos % 3) != 0:
        pos += 1
    elif char == 'U' and pos > 3:
        pos -= 3
    elif char == 'D' and pos < 7:
        pos += 3
    return pos


def process_char_2(char, pos):
    if char == 'L' and pos not in [1, 2, 5, 10, 13]:
        pos -= 1
    elif char == 'R' and pos not in [1, 4, 9, 12, 13]:
        pos += 1
    elif char == 'U' and pos not in [5, 2, 1, 4, 9]:
        if pos in [3, 13]:
            pos -= 2
        else:
            pos -= 4
    elif char == 'D' and pos not in [5, 10, 13, 12, 9]:
        if pos in [1, 11]:
            pos += 2
        else:
            pos += 4
    return pos


def process_char(char, pos, phase):
    if phase == 1:
        return process_char_1(char, pos)
    else:
        return process_char_2(char, pos)


def process_line(line, pos, phase):
    for char in line.strip():
        pos = process_char(char, pos, phase)
    return pos


def main():
    lines = readinput(sys.argv[1])

    code = []
    pos = 5
    for line in lines:
        pos = process_line(line, pos, 1)
        code.append(pos)

    print('Step 1: ' + ''.join([str(c) for c in code]))

    code = []
    pos = 5
    for line in lines:
        pos = process_line(line, pos, 2)
        code.append(pos)

    print('Step 2: ' + ''.join([hex(c)[2:] for c in code]))


if __name__ == "__main__":
    main()
