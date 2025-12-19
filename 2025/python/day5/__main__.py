from collections.abc import Iterable
from itertools import count

from utils.file import read_input




def main() -> None:
    lines = read_input(__package__)
    fresh_ranges = []
    ingredients = []
    for line in lines:
        if "-" in line:
            start_str, end_str = line.split("-", maxsplit=1)
            fresh_ranges.append((int(start_str), int(end_str)))
        else:
            ingredients.append(int(line))

    fresh_count = 0
    for available in ingredients:
        for start, end in fresh_ranges:
            if start <= available <= end:
                fresh_count += 1
                break
    print(fresh_count)

    fresh_ranges = sorted(fresh_ranges, key=lambda x: x[0])
    compacted_ranges = []
    for start, end in fresh_ranges:
        if not compacted_ranges or compacted_ranges[-1][1] + 1 < start:
            compacted_ranges.append((start, end))
        else:
            compacted_ranges[-1] = (compacted_ranges[-1][0], max(compacted_ranges[-1][1], end))
    print(sum(
    end - start + 1 for start, end in compacted_ranges
    ))




if __name__ == "__main__":
    main()
