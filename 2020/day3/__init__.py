import math
from typing import List

from utils import int_lines, int_list_lines, str_lines, str_list_lines

parse_input = int_list_lines(',')
parse_input = str_list_lines('\t')
parse_input = int_lines
parse_input = str_lines


def n_trees(grid: List[str], sx: int = 3, sy: int = 1) -> int:
    height = len(grid)
    width = len(grid[0])
    x, y = 0, 0
    trees = 0
    while y < height - 1:
        x, y = x + sx, y + sy
        if grid[y][x % width] == '#':
            trees += 1
    return trees


def p1(grid):
    return n_trees(grid)


def p2(grid):
    return math.prod([
        n_trees(grid, 1, 1),
        n_trees(grid, 3, 1),
        n_trees(grid, 5, 1),
        n_trees(grid, 7, 1),
        n_trees(grid, 1, 2)
    ])
