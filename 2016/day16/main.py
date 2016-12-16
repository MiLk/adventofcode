import sys
import string


def step(data):
    a = data
    b = a[::-1].translate(string.maketrans("01", "10"))
    return a + "0" + b


def checksum(data):
    s = ""
    for i in xrange(0, len(data) - 1, 2):
        if data[i] == data[i+1]:
            s += "1"
        else:
            s += "0"
    l = len(s)
    if l % 2 == 0:
        return checksum(s)
    else:
        return s


def main():
    init = sys.argv[1]
    disk_size = int(sys.argv[2])

    data = init
    while len(data) < disk_size:
        data = step(data)

    print('Checksum: %s' % checksum(data[:disk_size]))


if __name__ == "__main__":
    main()
