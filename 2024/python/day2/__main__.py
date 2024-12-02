from utils.file import int_list_line, read_input


def is_safe(levels: list[int]) -> bool:
    size = len(levels)
    ordered = all(levels[i] <= levels[i + 1] for i in range(size - 1)) or all(
        levels[i] >= levels[i + 1] for i in range(size - 1)
    )
    if not ordered:
        return False
    return all(1 <= abs(levels[i] - levels[i + 1]) <= 3 for i in range(size - 1))


def is_safe_with_dampener(levels: list[int]) -> bool:
    size = len(levels)
    if is_safe(levels):
        return True

    return any(is_safe(levels[:i] + levels[i + 1 :]) for i in range(size))


def main() -> None:
    lines = [int_list_line(l, " ") for l in read_input(__package__)]
    safe_reports = list(filter(is_safe, lines))

    print("Part 1:", len(safe_reports))
    safe_reports_with_dampener = list(filter(is_safe_with_dampener, lines))
    print("Part 2:", len(safe_reports_with_dampener))


if __name__ == "__main__":
    main()
