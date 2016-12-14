import sys
import hashlib
import re


def myhash(salt, index, stretch=0):
    string = salt + str(index)
    h = hashlib.md5(string).hexdigest()
    for i in xrange(0, stretch):
        h = hashlib.md5(h).hexdigest()
    return h


def solve(salt, stretch=0):
    reg = re.compile(r"(\w)\1\1")

    verified = {}
    futures = {}

    index = 0
    while len(verified) < 64:
        h = None
        if index in futures:
            h = futures[index]
        else:
            h = myhash(salt, index, stretch)

        m = reg.findall(h)
        if not m:
            index += 1
            continue

        for i in xrange(index + 1, index + 1001):
            h_v = None
            if i in futures:
                h_v = futures[i]
            else:
                h_v = myhash(salt, i, stretch)
                futures[i] = h_v

            if (m[0] * 5) in h_v:
                verified[index] = (h, (i, h_v))

        index += 1
    return verified


def main():
    salt = sys.argv[1]

    verified = solve(salt)
    keys = sorted(verified.keys())
    print('Step 1: %d' % keys[-1])
    verified = solve(salt, 2016)
    keys = sorted(verified.keys())
    print('Step 2: %d' % keys[-1])


if __name__ == "__main__":
    main()
