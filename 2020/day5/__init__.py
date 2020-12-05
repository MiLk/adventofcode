from utils import int_lines, int_list_lines, str_lines, str_list_lines

parse_input = str_lines


def row(s: str) -> int:
    r = 0
    for i in range(7):
        if s[i] == 'B':
            r += 2 ** (6 - i)
    return r

def col(s: str) -> int:
    c = 0
    for i in range(3):
        if s[7 + i] == 'R':
            c += 2 ** (2 - i)
    return c

def seat_id(s: str) -> int:
    return row(s) * 8 + col(s)


def p1(lines):
    print(seat_id('FBFBBFFRLR'))
    print(seat_id('BFFFBBFRRR'))
    print(seat_id('FFFBBBFRRR'))
    print(seat_id('BBFFBBFRLL'))

    return max(
        seat_id(l) for l in lines
    )


def p2(lines):
    seats = {seat_id(l) for l in lines}
    for i in range(2, max(seats)):
        if i not in seats and (i - 1) in seats and (i + 1) in seats:
            return i
