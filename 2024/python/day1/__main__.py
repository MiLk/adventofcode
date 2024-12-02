from collections import Counter

from utils.file import read_input


def main() -> None:
    lines = read_input(__package__)
    l1 = sorted(int(line[:5]) for line in lines)
    l2 = sorted(int(line[8:14]) for line in lines)

    distance = sum(abs(a - b) for a, b in zip(l1, l2))
    print("Part 1:", distance)

    c = Counter(l2)
    similarity = sum(n * c[n] for n in set(l1))
    print("Part 2:", similarity)


if __name__ == "__main__":
    main()
