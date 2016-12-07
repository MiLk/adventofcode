import sys


def readinput(path):
    if not path:
        path = 'input.txt'
    with open(path) as f:
        lines = f.readlines()
    return lines


def filter_line2(line):
    line = line.strip()
    in_brackets = False
    in_found = []
    out_found = []
    for i in xrange(0, len(line) - 2):
        if line[i] == '[':
            in_brackets = True
            continue
        elif line[i] == ']':
            in_brackets = False
            continue
        if line[i] == line[i+2] and line[i] != line[i+1]:
            if in_brackets:
                in_found.append(line[i:i+1])
            else:
                out_found.append(line[i:i+1])

    if in_found and out_found:
        for aba in in_found:
            for bab in out_found:
                if aba == bab[::-1]:
                    return True
    return False


def filter_line(line):
    line = line.strip()
    in_brackets = False
    found = []
    for i in xrange(0, len(line) - 3):
        if line[i] == '[':
            in_brackets = True
        elif line[i] == ']':
            in_brackets = False
        if line[i:i+2] == line[i+3:i+1:-1] and line[i] != line[i+1]:
            found.append(in_brackets)
    return False in found and True not in found


def main():
    lines = readinput(sys.argv[1])
    filtered = filter(filter_line, lines)
    print("Step 1: %d" % len(filtered))
    filtered = filter(filter_line2, lines)
    print("Step 2: %d" % len(filtered))


if __name__ == "__main__":
    main()
