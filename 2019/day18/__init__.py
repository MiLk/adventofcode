import itertools
import math
from functools import lru_cache

from utils import str_lines
from .astar import AStar

parse_input = str_lines


class MazeSolver(AStar):

    def __init__(self, maze, keys):
        self.maze = maze
        self.keys = keys
        self.width = len(maze[0])
        self.height = len(maze)

    @lru_cache
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

    def is_wall(self, x, y):
        if (c := self.maze[y][x]) == '#':
            return True
        if 'A' <= c <= 'Z' and c.lower() not in self.keys:
            return True

    def neighbors(self, node):
        """ for a given coordinate in the maze, returns up to 4 adjacent nodes that can be reached (=any adjacent coordinate that is not a wall)
        """
        x, y = node
        for i, j in [(0, -1), (0, +1), (-1, 0), (+1, 0)]:
            x1, y1 = x + i, y + j
            if 0 < x1 < self.width and 0 < y1 < self.height:
                if not self.is_wall(x1, y1):
                    yield x1, y1


def p1(lines):
    entrance = next((
        (x, y)
        for x, y in itertools.product(range(len(lines[0])), range(len(lines)))
        if lines[y][x] == '@'
    ), None)
    keys = {
        lines[y][x]: (x, y)
        for x, y in itertools.product(range(len(lines[0])), range(len(lines)))
        if 'a' <= lines[y][x] <= 'z'
    }


    def bfs_loop(queue):
        solved = []
        seen = set()
        m = 3079
        while queue:
            queue = list(sorted(queue, key=lambda x: (x[1] + 350 * (26 - len(x[0])))))
            item = queue.pop(0)
            visited, distance, start = item
            if visited in seen:
                continue
            seen.add(visited)
            print(f"{len(seen)} - {len(queue)} - {m=} - {len(visited)}")
            if distance >= m:
                continue
            if len(visited) == len(keys.keys()):
                print("solved", visited, distance)
                m = min(m, distance)
                solved.append((visited, distance))
            queue.extend(r for r in bfs(visited, distance, start) if r[1] < m)
        return solved

    def bfs(visited, distance, start):
        solved = []
        for name, pos in keys.items():
            if name in visited:
                continue
            if path_length := find_path(visited, start, pos):
                solved.append((visited + name,  distance + path_length - 1, pos))
        return solved

    global bestdfs
    bestdfs = 10000

    @lru_cache(maxsize=100000)
    def find_path(visited, start, pos):
        path = MazeSolver(lines, visited).astar(start, pos)
        return len(path) if path else 0

    def dfs(visited, distance, start):
        global bestdfs

        if distance >= bestdfs:
            return

        if len(visited) == len(keys.items()):
            bestdfs = min(bestdfs, distance)
            print(visited, distance, bestdfs)
            yield visited, distance

        for name, pos in keys.items():
            if name in visited:
                continue
            if path_length := find_path(visited, start, pos):
                for p, d in dfs(visited + name, distance + path_length - 1, pos):
                    yield p, d

    #solved = list(dfs('', 0, entrance))
    #print(solved)
    #print(min(l for _, l in solved))

    solved = bfs_loop([('', 0, entrance)])
    print(solved)
    print(min(l for _, l in solved))
    return


def p2(lines):
    return lines
