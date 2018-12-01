def read_input():
    with open('input.txt') as f:
        lines = f.readlines()
    return lines


def solve(argv, process_line, p1, p2):
    text_input = [argv[1]] if len(argv) > 1 else read_input()
    lines = list(map(process_line, text_input))

    s1 = p1(lines)
    print('Part 1:', s1)

    s2 = p2(lines)
    print('Part 2:', s2)


def int_line(line):
    return int(line.strip())


def int_list_line(line, sep='\t'):
    return [int(n) for n in line.strip().split(sep)]
