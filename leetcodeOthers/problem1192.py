from collections import defaultdict
from typing import Dict, List, Set


def get_cc(n, edges: Dict[int, Set[int]]) -> List[List[int]]:
    """
    :param n: number of vertices
    :param edges: mapping from vertex to set of neighboring vertices
    :return: list of cut edges
    """
    visit_time = [None] * n
    output = []
    curr_index = 0

    def dfs(u: int, parent=None) -> int:
        """
        :param u: unvisited vertex
        :param parent: parent of "u" vertex
        :return: in case u is part of a cycle, it is time = time of that ancestor
                 through which DFS enters the cycle. Else it is time at which DFS visits
                 the vertex "u"
        """
        nonlocal curr_index
        visited_time_of_u = curr_index
        curr_index += 1

        visit_time[u] = visited_time_of_u

        for v in edges[u]:
            if v != parent:
                if visit_time[v] is None:
                    t = dfs(v, parent=u)

                    if visited_time_of_u < t:  # no loop possible
                        output.append([u, v])

                visit_time[u] = min(visit_time[u], visit_time[v])

        return visit_time[u]

    for i in range(n):
        if visit_time[i] is None:  # unvisited vertex
            dfs(i)

    return output


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        """
        listing all the cut-edges of graph.

        An edge is a cut-edge <=> it belongs to no-cycle

        :param n: number of vertices
        :param connections: list of edge (edge = list of size two representing end vertices)
        :return: list of cut edges
        """

        edges = defaultdict(set)

        for u, v in connections:
            edges[u].add(v)
            edges[v].add(u)

        return get_cc(n, edges)
