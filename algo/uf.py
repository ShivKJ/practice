from dataclasses import dataclass
from functools import cached_property


@dataclass
class UF:
    """
    Implementing union find algorithm
    """
    node_count: int

    def find(self, u: int) -> int:
        """
        :return: representative node of cluster containing node u
        """
        return self._root(u)

    def union(self, u, v):
        """
        merging clustering containing node u and node v
        :param u:
        :param v:
        """
        u = self._root(u)
        v = self._root(v)

        self._update_rank(u, v)

    @property
    def clusters(self):
        """
        :return: number of clusters
        """
        return len(set(self._root(u) for u in range(self.node_count)))

    def _update_rank(self, u, v):
        """
        u and v are root nodes of two different clusters. In this function
        we determine which node should be made parent using rank.

        node with higher rank is made parent and in case of tie, the second
        (first can also be chosen) node is chosen and its rank is incremented
        by 1
        :param u:
        :param v:
        """
        rank = self._rank

        if rank[u] > rank[v]:
            self._parent[v] = u
        else:
            self._parent[u] = v
            if rank[u] == rank[v]:
                self._rank[v] += 1

    def _root(self, u: int) -> int:
        """
        :param u:
        :return: representative node of cluster containing node u
        """
        p = self._parent

        if u != p[u]:
            p[u] = self._root(p[u])

        return p[u]

    @cached_property
    def _parent(self):
        """
        :return: list in which ith index is the ith element and value
                 is its corresponding parent
        """
        return list(range(self.node_count))

    @cached_property
    def _rank(self):
        """
        :return: list in which ith index is ith node element and value
        is its rank. Rank is used when we merge two clusters
        """
        return [1] * self.node_count
