def int_lines(lines):
    return [int(l.strip()) for l in lines]


def int_list_lines(sep=None):
    return lambda lines: [
        int(n)
        for line in lines
        for n in line.strip().split(sep)
    ]


def str_lines(lines):
    return [l.strip() for l in lines]


def str_list_lines(sep=None):
    return lambda lines: [
        c
        for line in lines
        for c in line.strip().split(sep)
    ]
