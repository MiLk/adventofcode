import sys
import re


def readinput(path):
    if not path:
        path = 'input.txt'
    with open(path) as f:
        lines = f.readlines()
    return lines


def process_line(line):
    m = re.search('^([a-z-]+)-([0-9]+)\[([a-z]+)\]$', line)
    return m.groups()


def is_valid(room):
    (name, sector, checksum) = room
    count = dict()
    for char in name:
        if char == '-':
            continue
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    def sort(x, y):
        if count[x] == count[y]:
            return ord(x) - ord(y)
        else:
            return count[y] - count[x]

    checksum2 = ''.join(sorted(count.keys(), sort)[0:5])
    return checksum == checksum2


def decypher(room):
    (encrypted, sector, _) = room
    shift = int(sector)

    def rot(char):
        if char == '-':
            return ' '
        else:
            return chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))

    plain = ''.join(map(rot, encrypted))
    return (plain, sector)


def main():
    lines = readinput(sys.argv[1])
    rooms = [process_line(line.strip()) for line in lines]
    real_rooms = filter(is_valid, rooms)
    sector_sum = reduce((lambda acc, r: acc + int(r[1])), real_rooms, 0)
    print('Part 1: %d' % sector_sum)

    decyphered = [decypher(room) for room in real_rooms]
    for room in decyphered:
        if room[0].find('north') > -1 and room[0].find('pole') > -1:
            print('Part 2: %s' % room[1])


if __name__ == "__main__":
    main()
