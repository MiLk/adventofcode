import asyncio
import re
from collections import defaultdict

from utils.file import read_input

LABEL_RE = re.compile(r"^(\w+)[-=].*")


def hash_step(s: str) -> int:
    v = 0
    for c in s:
        v += ord(c)
        v = (v * 17) % 256
    return v


async def main() -> None:
    lines = read_input(__package__, strip=False)
    init_seq = lines[0].strip().split(",")
    # init_seq = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7".split(",")
    print("Part 1:", sum(hash_step(v) for v in init_seq))

    boxes: defaultdict[int, list[tuple[str, int]]] = defaultdict(list)
    for step in init_seq:
        m = LABEL_RE.match(step)
        assert m
        label = m.group(1)
        box = hash_step(label)
        operation = step[len(label)]
        rest = step[len(label) + 1 :]
        lenses = boxes[box]
        if operation == "=":
            if (existing := next((i for i, (l, _) in enumerate(lenses) if l == label), None)) is not None:
                boxes[box][existing] = (label, int(rest))
            else:
                boxes[box].append((label, int(rest)))
        elif operation == "-":
            boxes[box] = [l for l in lenses if l[0] != label]

    print("Part 2:", sum((1 + n) * i * f for n, lenses in boxes.items() for i, (_, f) in enumerate(lenses, start=1)))


if __name__ == "__main__":
    asyncio.run(main())
