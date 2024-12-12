from operator import attrgetter, itemgetter

from utils.file import read_input

plots = {complex(x, y): c for y, line in enumerate(read_input(__package__)) for x, c in enumerate(line)}


def flood(start: complex) -> tuple[str, set[complex]]:
    region_name = plots[start]
    visited: set[complex] = set()
    queue: list[complex] = [start]
    while queue:
        current = queue.pop()
        if current in visited or plots.get(current) != region_name:
            continue
        visited.add(current)
        queue.extend(current + d for d in {-1, 1, -1j, 1j})
    return region_name, visited


def perimeter(region: set[complex]) -> int:
    return sum(plot + d not in region for plot in region for d in {-1, 1, -1j, 1j})


def find_regions() -> list[tuple[str, set[complex]]]:
    visited_plots: set[complex] = set()
    result: list[tuple[str, set[complex]]] = []

    sorted_plots = sorted(plots, key=lambda p: (p.real, p.imag))
    while sorted_plots:
        current = sorted_plots.pop()
        if current in visited_plots:
            continue
        name, region = flood(current)
        visited_plots |= region
        result.append((name, region))

    return result


regions = find_regions()
print("Part1:", sum(perimeter(region) * len(region) for _, region in regions))
