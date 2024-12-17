from utils.file import read_input

DIRECTIONS = {"<": -1, ">": 1, "^": -1j, "v": 1j}

lines = read_input(__package__)
warehouse = {complex(x, y): c for y, line in enumerate(lines) if line[0] == "#" for x, c in enumerate(line)}
movements = [DIRECTIONS[c] for line in lines if line[0] in DIRECTIONS for c in line]
robot = next((p for p, c in warehouse.items() if c == "@"), None)
assert robot is not None


def push_boxes(start: complex, movement: complex) -> bool:
    current = start
    while True:
        current = current + movement
        content = warehouse.get(current)
        if content == "#":
            return False
        elif content in {".", "@"}:
            warehouse[start] = "."
            warehouse[current] = "O"
            return True


for i, m in enumerate(movements):
    # print(f"Step {i}", m)
    # for y in range(len(lines)):
    #        print(''.join(warehouse.get(complex(x, y), '.') for x in range(len(lines[0]))))
    new_position = robot + m
    if warehouse.get(new_position) == "#":
        continue
    if warehouse.get(new_position) == "O":
        if not push_boxes(new_position, m):
            continue
    warehouse[robot] = "."
    robot = new_position
    warehouse[robot] = "@"

for y in range(len(lines)):
    print("".join(warehouse.get(complex(x, y), ".") for x in range(len(lines[0]))))

print("Part1:", sum(int(100 * p.imag + p.real) for p, c in warehouse.items() if c == "O"))
