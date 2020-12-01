def int_lines(lines):
    return [int(l.strip()) for l in lines]


def int_list_lines(sep=None):
    return lambda lines: [[int(n) for n in line.strip().split(sep)] for line in lines]


def str_lines(lines):
    return [l.strip() for l in lines]


def str_list_lines(sep=None):
    return lambda lines: [line.strip().split(sep) for line in lines]
