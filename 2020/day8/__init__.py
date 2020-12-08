def parse_input(lines):
    return [
        (line[:3], line[4:].strip())
        for line in lines
    ]


def p1(instructions):
    ipc = 0
    acc = 0
    executed = set()
    while True:
        if ipc in executed:
            return acc

        executed.add(ipc)
        op, arg = instructions[ipc]
        if op == 'acc':
            acc += int(arg)
        elif op == 'jmp':
            ipc += int(arg)
            continue
        elif op == 'nop':
            pass
        else:
            raise NotImplementedError
        ipc += 1


def run_with_replacement(instructions, c):
    ipc = 0
    acc = 0
    executed = set()
    while True:
        if ipc >= len(instructions):
            break

        if ipc in executed:
            return None

        executed.add(ipc)
        op, arg = instructions[ipc]

        if ipc == c:
            op = "nop" if op == "jmp" else "jmp"

        if op == 'acc':
            acc += int(arg)
        elif op == 'jmp':
            ipc += int(arg)
            continue
        elif op == 'nop':
            pass
        else:
            raise NotImplementedError
        ipc += 1
    return acc


def p2(instructions):
    ipc = 0
    executed = set()
    candidates = set()
    while True:
        if ipc in executed:
            break

        executed.add(ipc)
        op, arg = instructions[ipc]

        if op in ['jmp', 'nop']:
            candidates.add(ipc)

        if op == 'jmp':
            ipc += int(arg)
            continue
        elif op in ['acc', 'nop']:
            pass
        else:
            raise NotImplementedError
        ipc += 1

    for c in candidates:
        if acc := run_with_replacement(instructions, c):
            return acc


