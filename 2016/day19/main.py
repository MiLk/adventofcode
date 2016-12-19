import sys


def solve(presents):
    while len(presents) > 1:
        removed = set()
        for i in xrange(0, len(presents)):
            elf = presents[i]
            if elf[1] == 0:
                continue
            next_elf = (i+1) % len(presents)
            nb = elf[1] + presents[next_elf][1]
            presents[next_elf] = (presents[next_elf][0], 0)
            presents[i] = (elf[0], nb)
            removed.add(next_elf)
        presents = filter(lambda e: e[1] != 0, presents)

    print('Step 1: %d' % presents[0][0])


def main():
    elves = int(sys.argv[1])
    presents = []
    for i in xrange(0, elves):
        presents.append((i + 1, 1))
    solve(presents)

    i = 1
    while i * 3 < elves:
        i *= 3
    print('Step 2: %d' % (elves - i))

if __name__ == "__main__":
    main()
