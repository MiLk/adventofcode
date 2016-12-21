import sys


def readinput(path):
    if not path:
        path = 'input.txt'
    with open(path) as f:
        lines = f.readlines()
    return lines


def process_line(line):
    l = line.strip().split('-')
    return (int(l[0]), int(l[1]))


def slow(ips):
    from interval import Interval, IntervalSet
    r1 = IntervalSet([Interval(0, 4294967295)])
    r2 = IntervalSet([Interval(ip[0], ip[1]) for ip in ips])
    diff = r1 - r2
    total = 0
    for i in diff:
        start = i.lower_bound + 1
        total += i.upper_bound - start
    print('Part 2: %d' % total)


def main():
    lines = readinput(sys.argv[1])
    lines = map(process_line, lines)
    ips = sorted(lines, key=lambda i: int(i[0]))
    lower = 0
    for ip in ips:
        start, end = ip
        if start > lower:
            break
        lower = max(lower, end + 1)

    print('Part 1: %d' % lower)

    allowed = []
    last = 0
    for ip in ips:
        start, end = ip
        if start > last:
            allowed.append((last, start-1))
        last = max(last, end + 1)

    allowed.append((last, 4294967295))
    total = 0
    for a in allowed:
        total += a[1] - a[0] + 1

    print('Part 2: %d' % total)


if __name__ == "__main__":
    main()
