import sys


def readinput(path):
    if not path:
        path = 'input.txt'
    with open(path) as f:
        lines = f.readlines()
    return lines


def process_line(line):
    parts = line.strip().split(' ')
    if len(parts) == 2:
        return (parts[0], parts[1], None)
    else:
        return (parts[0], parts[1], parts[2])


def process_instruction(instruction, r, ip):
    cmd, op1, op2 = instruction
    if cmd == 'inc':
        r[op1] += 1
    elif cmd == 'dec':
        r[op1] -= 1
    elif cmd == 'cpy':
        if op1 in r.keys():
            r[op2] = r[op1]
        else:
            r[op2] = int(op1)
    elif cmd == 'jnz':
        x = op1
        if x in r.keys():
            x = r[x]
        else:
            x = int(x)
        if x != 0:
            return r, ip + int(op2)
    elif cmd == 'out':
        r['out'] += str(r[op1])
    return r, ip + 1


def main():
    lines = readinput(sys.argv[1])
    lines = map(process_line, lines)

    solution = None

    import itertools
    for i in itertools.count():
        # registers
        r = {'a': i, 'b': 0, 'c': 0, 'd': 0, 'out': ''}
        
        ip = 0  # instruction pointer
        while ip < len(lines) and not solution:
            instruction = lines[ip]
            r, ip = process_instruction(instruction, r, ip)
            if len(r['out']) > 2 and r['out'][-1] == r['out'][-2]:
                break
            if len(r['out']) >= 50:
                solution = i
                break

        if solution:
            break

    print('Part 1: %d', solution)

if __name__ == "__main__":
    main()
