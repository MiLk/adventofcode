import sys
import operator


def readinput(path):
    if not path:
        path = 'input.txt'
    with open(path) as f:
        lines = f.readlines()
    return lines


def main():
    lines = readinput(sys.argv[1])
    size = len(lines[0].strip())
    count = {}
    itr = xrange(0, size)
    for i in itr:
        count[i] = {}
    for line in lines:
        for i in itr:
            char = line[i]
            if char not in count[i]:
                count[i][char] = 1
            else:
                count[i][char] += 1

    message = ""
    message2 = ""
    for pos, stats in count.iteritems():
        char = max(stats.iteritems(), key=operator.itemgetter(1))[0]
        char2 = min(stats.iteritems(), key=operator.itemgetter(1))[0]
        message += char
        message2 += char2

    print('Part 1: %s' % message)
    print('Part 2: %s' % message2)


if __name__ == "__main__":
    main()
