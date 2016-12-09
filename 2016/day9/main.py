import sys
import re


def readinput(path):
    if not path:
        path = 'input.txt'
    with open(path) as f:
        lines = f.readlines()
    return lines


def process_content(content):
    if content[0] != '(':
        end = content.find('(')
        if end == -1:
            return content, ''
        else:
            return (content[:end], content[end:])

    m = re.match('^\((\d+)x(\d+)\)', content)
    length, repeat = m.groups()
    left = content[len(length)+len(repeat)+3:]
    length = int(length)
    repeat = int(repeat)
    return left[:length] * repeat, left[length:]


def process_length(content):
    if not content:
        return 0
    if content[0] != '(':
        end = content.find('(')
        if end == -1:
            return len(content)
        else:
            return len(content[:end]) + process_length(content[end:])

    m = re.match('^\((\d+)x(\d+)\)', content)
    length, repeat = m.groups()
    left = content[len(length)+len(repeat)+3:]
    length = int(length)
    repeat = int(repeat)
    string = left[:length]
    if string.find('('):
        return len(string) * repeat + process_length(left[length:])
    else:
        return process_length(left[:length]) * repeat + \
                process_length(left[length:])


def main():
    lines = readinput(sys.argv[1])
    content = lines[0].strip()

    answer = ""
    while content:
        out, content = process_content(content)
        answer += out

    print('Step 1: %d' % len(answer))

    answer = process_length(answer)
    print('Step 2: %d' % answer)

if __name__ == "__main__":
    main()
