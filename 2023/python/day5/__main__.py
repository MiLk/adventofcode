from collections.abc import Iterable
from itertools import batched
from operator import itemgetter
from typing import Callable

from utils.file import read_input

DataMap = list[tuple[int, int, int]]


def build_data_map(lines: list[str]) -> tuple[list[int], dict[str, DataMap]]:
    seeds: list[int] = []
    current_map: str = ""
    data_map: dict[str, DataMap] = {}
    for line in lines:
        if line.startswith("seeds:"):
            seeds = list(map(int, line[7:].split(" ")))
        elif line.endswith("map:"):
            current_map = line[: line.find(" ")]
            data_map[current_map] = []
        else:
            dest_range_start, src_range_start, range_length = map(int, line.split(" "))
            data_map[current_map].append((dest_range_start, src_range_start, range_length))

    sorted_data_map: dict[str, DataMap] = {}
    for k, v in data_map.items():
        sorted_data_map[k] = sorted(v, key=itemgetter(1))

    return seeds, sorted_data_map


def find_location_for_seed(sorted_data_map: dict[str, DataMap]) -> Callable[[int], int]:
    def _do(seed_number: int) -> int:
        return find_destination(
            sorted_data_map["humidity-to-location"],
            find_destination(
                sorted_data_map["temperature-to-humidity"],
                find_destination(
                    sorted_data_map["light-to-temperature"],
                    find_destination(
                        sorted_data_map["water-to-light"],
                        find_destination(
                            sorted_data_map["fertilizer-to-water"],
                            find_destination(
                                sorted_data_map["soil-to-fertilizer"],
                                find_destination(sorted_data_map["seed-to-soil"], seed_number),
                            ),
                        ),
                    ),
                ),
            ),
        )

    return _do


def find_destination(data_map: DataMap, source: int) -> int:
    return next(
        (
            dest_range_start + source - src_range_start
            for dest_range_start, src_range_start, range_length in data_map
            if src_range_start <= source < src_range_start + range_length
        ),
        source,
    )


def find_destination_for_range(data_map: DataMap, source_range: tuple[int, int]) -> Iterable[tuple[int, int]]:
    current_range, next_range = next(
        (
            (source_range[0], src_range_start + range_length)
            for dest_range_start, src_range_start, range_length in data_map
            if src_range_start <= source_range[0] < src_range_start + range_length
        ),
        (source_range[0], None),
    )
    if not next_range:
        # we didn't find a range matching the start of our source range
        # let's look for the smallest one following it
        # if there is one, it becomes the start of the next range
        # if the is none, we put a value larger than the end of the source range
        next_range = next((srs for _, srs, _ in data_map if srs > source_range[0]), source_range[1] + 1)
    if source_range[1] < next_range:
        yield find_destination(data_map, source_range[0]), find_destination(data_map, source_range[1])
        return

    yield find_destination(data_map, source_range[0]), find_destination(data_map, next_range - 1)
    yield from find_destination_for_range(data_map, (next_range, source_range[1]))


def main() -> None:
    lines = read_input(__package__)
    seeds, sorted_data_map = build_data_map(lines)

    seed_to_location = map(find_location_for_seed(sorted_data_map), seeds)
    print("Part 1:", min(seed_to_location))

    seed_ranges = [(s, s + l - 1) for s, l in batched(seeds, n=2)]  # inclusive range
    soil_ranges = [r for x in seed_ranges for r in find_destination_for_range(sorted_data_map["seed-to-soil"], x)]
    fertilizer_ranges = [
        r for x in soil_ranges for r in find_destination_for_range(sorted_data_map["soil-to-fertilizer"], x)
    ]
    water_ranges = [
        r for x in fertilizer_ranges for r in find_destination_for_range(sorted_data_map["fertilizer-to-water"], x)
    ]
    light_ranges = [r for x in water_ranges for r in find_destination_for_range(sorted_data_map["water-to-light"], x)]
    temperature_ranges = [
        r for x in light_ranges for r in find_destination_for_range(sorted_data_map["light-to-temperature"], x)
    ]
    humidity_ranges = [
        r for x in temperature_ranges for r in find_destination_for_range(sorted_data_map["temperature-to-humidity"], x)
    ]
    location_ranges = [
        r for x in humidity_ranges for r in find_destination_for_range(sorted_data_map["humidity-to-location"], x)
    ]
    print("Part 2:", min(location_ranges)[0])


if __name__ == "__main__":
    main()
