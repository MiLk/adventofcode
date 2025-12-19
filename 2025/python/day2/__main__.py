from utils.file import read_input


def has_repetition(n: int) -> bool:
    """Check if the integer n is made only of some sequence of digits repeated."""
    s = str(n)
    length = len(s)
    for i in range(1, length // 2 + 1):
        if length % i == 0:
            if s[:i] * (length // i) == s:
                return True
    return False


def has_repetition_twice(n: int) -> bool:
    """Check if the integer n is made only of some sequence of digits repeated twice."""
    s = str(n)
    length = len(s)
    if length % 2 != 0:
        return False
    mid = length // 2
    return s[:mid] == s[-mid:]


def main() -> None:
    lines = read_input(__package__)
    ranges = [tuple(int(n) for n in range_.split("-", maxsplit=2)) for range_ in lines[0].split(",")]
    invalid_ids = []
    for start, end in ranges:
        for id_ in range(start, end + 1):
            # Part 1
            # if has_repetition_twice(id_):
            #    invalid_ids.append(id_)
            # Part 2
            if has_repetition(id_):
                invalid_ids.append(id_)
    print(invalid_ids)
    print(sum(invalid_ids))


if __name__ == "__main__":
    main()
