from collections import OrderedDict
from math import floor

from utils.file import read_input

disk_map = list(map(int, read_input(__package__)[0]))


def p1() -> int:
    uncompressed_disk_map: list[str] = []
    for i in range(floor((len(disk_map) + 1) / 2)):
        occupied = disk_map[i * 2]
        for _ in range(occupied):
            uncompressed_disk_map.append(str(i))
        try:
            free = disk_map[i * 2 + 1]
            for _ in range(free):
                uncompressed_disk_map.append(".")
        except IndexError:
            pass

    size = len(uncompressed_disk_map)
    if size < 100:
        print("".join(uncompressed_disk_map))

    while True:
        free_space = next(i for i in range(size) if uncompressed_disk_map[i] == ".")
        last_character = next(size - i for i in range(1, size) if uncompressed_disk_map[size - i].isdigit())
        if free_space > last_character:
            break
        uncompressed_disk_map[free_space], uncompressed_disk_map[last_character] = (
            uncompressed_disk_map[last_character],
            uncompressed_disk_map[free_space],
        )

    return sum(i * int(n) for i, n in enumerate(uncompressed_disk_map) if n != ".")


def p2() -> int:
    files = OrderedDict({i: disk_map[i * 2] for i in range(floor((len(disk_map) + 1) / 2))})

    reordered: list[tuple[int, int]] = []
    for i in range(floor((len(disk_map) + 1) / 2)):
        try:
            free = disk_map[i * 2 + 1]
        except IndexError:
            free = 0
        if i in files.keys():
            reordered.append((i, files[i]))
            del files[i]
            if not files:
                break
        else:
            reordered.append((-1, disk_map[i * 2]))

        while free > 0:
            n = next((n_ for n_, size in reversed(files.items()) if size <= free), None)
            if n is None:
                break
            consumed = files[n]
            reordered.append((n, consumed))
            free -= consumed
            del files[n]

            if not files:
                break

        if free > 0:
            reordered.append((-1, free))

    reordered_disk_map: list[str] = []
    for idx, length in reordered:
        for _ in range(length):
            reordered_disk_map.append(str(idx) if idx != -1 else ".")

    if len(reordered_disk_map) < 100:
        print("".join(reordered_disk_map))
    return sum(i * int(n) for i, n in enumerate(reordered_disk_map) if n != ".")


print("Part 1:", p1())
print("Part 2:", p2())
