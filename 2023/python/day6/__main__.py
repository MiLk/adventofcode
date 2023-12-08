import operator
from functools import reduce


def distance(hold: int, duration: int) -> int:
    return (duration - hold) * hold


def main() -> None:
    times = [41, 66, 72, 66]
    records = [244, 1047, 1228, 1040]

    win_ways: list[int] = [len([h for h in range(t) if distance(h, t) > r]) for t, r in zip(times, records)]
    print("Part 1:", reduce(operator.mul, win_ways))

    time = 41667266
    record = 244104712281040
    first_approx = next(h for h in range(0, time, 10) if distance(h, time) > record)
    first = next(h for h in range(first_approx - 10, time) if distance(h, time) > record)
    last_approx = next(h for h in range(0, time, 10) if distance(time - h, time) > record)
    last = next(time - h for h in range(last_approx - 10, time) if distance(time - h, time) > record)
    print("Part 2:", last - first + 1)


if __name__ == "__main__":
    main()
