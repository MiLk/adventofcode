#! /usr/bin/env python
# -*- coding: utf-8 -*-

""" generic A-Star path searching algorithm """

import sys
from abc import ABCMeta, abstractmethod

__author__ = "Julien Rialland"
__copyright__ = "Copyright 2012, J.Rialland"
__license__ = "BSD"
__version__ = "0.9"
__maintainer__ = __author__
__email__ = "julien.rialland@gmail.com"
__status__ = "Production"


class AStar:

    __metaclass__ = ABCMeta

    @abstractmethod
    def heuristic_cost_estimate(self, start, goal):
        """computes the estimated (rough) distance between two random nodes, this method must be implemented in a subclass"""
        raise NotImplementedError

    @abstractmethod
    def distance_between(self, n1, n2):
        """gives the real distance between two adjacent nodes n1 and n2 (i.e n2 belongs to the list of n1's neighbors), this method must be implemented in a subclass"""
        raise NotImplementedError

    @abstractmethod
    def neighbors(self, node):
        """for a given node, returns (or yields) the list of its neighbors. this method must be implemented in a subclass"""
        raise NotImplementedError

    def _yield_path(self, came_from, last):
        yield last
        current = came_from[last]
        while True:
            yield current
            if current in came_from:
                current = came_from[current]
            else:
                break

    def _reconstruct_path(self, came_from, last):
        return list(reversed([p for p in self._yield_path(came_from, last)]))

    def astar(self, start, goal, limit=None):
        """applies the a-star path searching algorithm in order to find a route between a 'start' node and a 'root' node"""
        closedset = set([])    # The set of nodes already evaluated.
        # The set of tentative nodes to be evaluated, initially containing the
        # start node
        openset = set([start])
        came_from = {}    # The map of navigated nodes.

        g_score = {}
        g_score[start] = 0   # Cost from start along best known path.

        # Estimated total cost from start to goal through y.
        f_score = {}
        f_score[start] = self.heuristic_cost_estimate(start, goal)

        while len(openset) > 0:
            # the node in openset having the lowest f_score[] value
            current = min(f_score, key=f_score.get)
            if goal and current == goal:
                return self._reconstruct_path(came_from, goal)
            openset.discard(current)  # remove current from openset
            del f_score[current]
            closedset.add(current)  # add current to closedset


            if limit and not goal and g_score[current] >= limit:
                continue

            for neighbor in self.neighbors(current):
                if neighbor in closedset:
                    continue
                tentative_g_score = g_score[
                    current] + self.distance_between(current, neighbor)
                if (neighbor not in openset) or (tentative_g_score < g_score[neighbor]):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + \
                        self.heuristic_cost_estimate(neighbor, goal)
                    openset.add(neighbor)

        return None

