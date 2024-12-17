import sys

from utils.file import read_input

lines = read_input(__package__)
registers = int(lines[0][12:]), int(lines[1][12:]), int(lines[2][12:])
program = tuple(map(int, lines[3][9:].split(",")))
end = len(program)


def run_program(ra: int, rb: int, rc: int) -> tuple[int, ...]:
    def combo(value: int) -> int:
        match value:
            case 4:
                return ra
            case 5:
                return rb
            case 6:
                return rc
            case 0 | 1 | 2 | 3:
                return value
            case _:
                raise ValueError(f"Invalid operand {value}")

    iptr = 0
    output: list[int] = []
    while iptr < end:
        opcode, operand = program[iptr], program[iptr + 1]
        match opcode:
            case 0:  # adv
                ra = ra // 2 ** combo(operand)
            case 1:  # bxl
                rb = rb ^ operand
            case 2:  # bst
                rb = combo(operand) % 8
            case 3 if ra != 0:  # jnz
                iptr = operand
                continue
            case 3:
                pass
            case 4:  # bxc
                rb = rb ^ rc
            case 5:  # out
                output.append(combo(operand) % 8)
            case 6:  # bdv
                rb = ra // 2 ** combo(operand)
            case 7:  # cdv
                rc = ra // 2 ** combo(operand)
            case _:
                return tuple()
        iptr += 2
    return tuple(output)


print("Part 1:", ",".join(map(str, run_program(*registers))))


def find_input(cursor: int, seed: int) -> int | None:
    for candidate in range(8):
        if run_program(seed * 8 + candidate, registers[1], registers[2]) != program[cursor:]:
            continue
        if cursor == 0:
            return seed * 8 + candidate
        if (result := find_input(cursor - 1, seed * 8 + candidate)) is not None:
            return result
    return None


print("Part 2:", find_input(len(program) - 1, 0))
