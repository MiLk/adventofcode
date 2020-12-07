from utils import int_lines, int_list_lines, str_lines, str_list_lines

parse_input = str_lines


def p1(lines):
    group = set()
    total = 0
    for line in lines:
        if not line:
            total += len(group)
            group = set()
            continue

        for c in line:
            group.add(c)
    return total + len(group)



def p2(lines):
    d = []
    group = None
    total = 0
    for line in lines:
        if not line:
            total += len(group)
            group = None
            d = []
            continue

        d.append(line)
        if group is not None:
            group = group.intersection(set(c for c in line))
        else:
            group = set(c for c in line)
    return total + len(group)
