from __future__ import print_function

import sys
import re
import math

from astar import AStar


def process_line(line):
    return line

def is_wall(x, y, favorite_number):
    s = x * x + 3 * x + 2 * x * y + y + y * y
    s += favorite_number
    binary = bin(s)
    occ = binary.count('1')
    return (occ % 2) == 1

def print_maze(fav, obj):
    for j in xrange(0, 40):
        for i in xrange(0, 40):
            if i == obj[0] and j == obj[1]:
                print('X', end='')
            if is_wall(i, j, fav):
                print('#', end='')
            else:
                print('.', end='')
        print('')


class MazeSolver(AStar):

    def __init__(self, fav):
        self.width = 60
        self.height = 60
        self.fav = fav

    def heuristic_cost_estimate(self, n1, n2):
        """computes the 'direct' distance between two (x,y) tuples"""
        if not n1 or not n2:
            return 0
        (x1, y1) = n1
        (x2, y2) = n2
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def distance_between(self, n1, n2):
        """this method always returns 1, as two 'neighbors' are always adajcent"""
        return 1

    def neighbors(self, node):
        """ for a given coordinate in the maze, returns up to 4 adjacent nodes that can be reached (=any adjacent coordinate that is not a wall)
        """
        x, y = node
        for i, j in [(0, -1), (0, +1), (-1, 0), (+1, 0)]:
            x1 = x + i
            y1 = y + j
            if x1 > 0 and y1 > 0 and x1 < self.width and y1 < self.height:
                if not is_wall(x1, y1, self.fav):
                    yield (x1, y1)



def main():
    fav = int(sys.argv[1])
    obj = (int(sys.argv[2]), int(sys.argv[3]))
    start = (1,1)
    path, p2 = MazeSolver(fav).astar(start, obj, 50)
    print('Step 1: %d' % (len(path) -1))
    print('Step 2: %d' % len(p2))

    _, reached = MazeSolver(fav).astar(start, None, 50)
    if reached:
        print('Step 2: %d' % len(reached))


if __name__ == "__main__":
    main()
