import sys
import md5


def find_char(puzzle, index):
    while True:
        phrase = puzzle + str(index)
        digest = md5.new(phrase).hexdigest()
        index += 1
        if digest[0:5] == '00000':
            try:
                return int(digest[5]), digest[6], index
            except ValueError:
                continue


def main():
    puzzle = sys.argv[1]

    index = 0
    password = [0, 0, 0, 0, 0, 0, 0, 0]
    found = 0
    while found != 8:
        pos, char, index = find_char(puzzle, index)
        if pos not in range(0, 8):
            continue
        if password[pos] != 0:
            continue
        password[pos] = char
        found += 1

    print('Step 2: %s' % ''.join(password))


if __name__ == "__main__":
    main()
