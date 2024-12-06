from utils.file import read_input

lines = read_input(__package__)
height = len(lines)
width = len(lines[0])

start = next((i, line.index("^")) for i, line in enumerate(lines) if "^" in line)

obstacles = {complex(i, j) for i, line in enumerate(lines) for j, c in enumerate(line) if c == "#"}

directions = [-1, 1j, 1, -1j]


def walk(pos: complex, obstacles_: set[complex]) -> tuple[set[complex], bool]:
    direction = 0
    path: set[complex] = {pos}
    visited: set[tuple[complex, int]] = {(pos, direction)}
    while True:
        new_pos = pos + directions[direction]
        if not (0 <= new_pos.real < height and 0 <= new_pos.imag < width):
            break
        if new_pos in obstacles_:
            direction = (direction + 1) % 4
            continue
        if (new_pos, direction) in visited:
            return path, True
        pos = new_pos
        path.add(pos)
        visited.add((pos, direction))
    return path, False


path, _ = walk(complex(*start), obstacles)
print("Part 1:", len(path))

result = 0
for i, candidate in enumerate(path):
    # print("Candidate", i, candidate)
    _path, loop = walk(complex(*start), obstacles | {candidate})
    if loop:
        result += 1

print("Part 2:", result)
