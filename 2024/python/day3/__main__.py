import re

from utils.file import read_input

MUL_INSTRUCTION_RE = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

program = "".join(read_input(__package__))
s = sum(int(m.group(1)) * int(m.group(2)) for m in MUL_INSTRUCTION_RE.finditer(program))

print("Part 1:", s)

enabled = True
s = 0
i = 0
while True:
    if not enabled:
        next_do = program.find("do()", i)
        if next_do == -1:
            break
        i = next_do + 4
        enabled = True
        continue

    next_mul = MUL_INSTRUCTION_RE.search(program, i)
    if next_mul is None:
        break
    next_dont = program.find("don't()", i)
    if next_dont > 0 and next_dont < next_mul.start():
        i = next_dont + 7
        enabled = False
        continue

    i = next_mul.end()
    s += int(next_mul.group(1)) * int(next_mul.group(2))

print("Part 2:", s)
