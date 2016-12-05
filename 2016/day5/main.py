import sys
import md5


def find_char(puzzle, index):
    while True:
        phrase = puzzle + str(index)
        digest = md5.new(phrase).hexdigest()
        index += 1
        if digest[0:5] == '00000':
            return digest[5], index


def main():
    puzzle = sys.argv[1]

    index = 0
    password = ""
    for i in xrange(0, 8):
        char, index = find_char(puzzle, index)
        password += char

    print('Step 1: %s' % password)


if __name__ == "__main__":
    main()
