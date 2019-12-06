from collections import defaultdict
from typing import List

from utils import str_list_lines


def parse_input(lines):
    orbits = [tuple(l) for l in str_list_lines(')')(lines)]
    return {
        child: parent
        for parent, child in orbits
    }


def p1(tree):
    def depth(o):
        if o not in tree:
            return 0
        return 1 + depth(tree[o])

    return sum(
        depth(o)
        for o in tree.keys()
    )


def p2(tree):
    def resolve_path(o) -> List[str]:
        if o not in tree:
            return []
        return resolve_path(tree[o]) + [o]

    p1, p2 = resolve_path('YOU'), resolve_path('SAN')
    common = sum(1 for a, b in zip(p1, p2) if a == b)
    return len(p1[common:-1]) + len(p2[common:-1])
