def parse_input(lines):
    def parse_line(line):
        po1, po2, pwd = line.split(' ', maxsplit=2)
        n1, n2 = po1.split('-', maxsplit=1)
        return int(n1), int(n2), po2[0], pwd

    return [parse_line(l.strip()) for l in lines]


def p1(lines):
    return sum(
        m1 <= p.count(c) <= m2
        for m1, m2, c, p in lines
    )


def p2(lines):
    def is_valid(m1, m2, c, p):
        if m1 > len(p) or m2 > len(p):
            return False
        a, b = p[m1 - 1], p[m2 - 1]
        return a != b and (a == c or b == c)

    return sum(
        is_valid(m1, m2, c, p)
        for m1, m2, c, p in lines
    )
