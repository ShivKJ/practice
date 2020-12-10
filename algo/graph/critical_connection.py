from dataclasses import dataclass, field
from functools import cached_property
from itertools import count
from typing import Dict, Hashable, List, Tuple


@dataclass(unsafe_hash=True)
class Vertex:
    """
    Defining vertex to be used in CriticalConnection (CC) algorithm
    """
    id: Hashable = field(hash=True)
    index: int = field(default=None, compare=False, init=False)  # index provided by CC algo
    low: int = field(default=None, compare=False, init=False)

    # to keep track if this vertex has been visited in DFS
    visited: bool = field(default=False, compare=False, init=False)

    # keeping pointer to get DFS parent of this vertex. In case DFS
    # starts from this vertex, it is its own parent
    parent: 'Vertex' = field(default=None, compare=False, init=False)

    def __str__(self):
        return f'Vertex(id={self.id}, index={self.index}, low={self.low}, parent={self.parent.id})'

    def __repr__(self):
        return str(self)


@dataclass
class CriticalConnection:
    """
    Given a graph, critical connections are those edges removal of which
    will increase connected components of graph
    """
    vertices: List[Vertex]
    edges: Dict[Vertex, List[Vertex]]

    def process(self) -> List[Tuple[Vertex, Vertex]]:
        """
        running DFS to find CC
        :return: list of edges representing CC
        """
        for v in self.vertices:
            if not v.visited:
                v.parent = v
                self._dfs(v)

        return self.output

    def _dfs(self, vertex: Vertex) -> int:
        """
        :param vertex:
        :return:
        """
        vertex.visited = True
        vertex.index = vertex.low = self._next_id

        for adj_vertex in self._adjacent_edges(vertex):
            if not adj_vertex.visited:
                adj_vertex.parent = vertex
                adj_low = self._dfs(adj_vertex)

                vertex.low = min(vertex.low, adj_low)  # parent low should be less than child low
            elif vertex.parent is not adj_vertex:
                vertex.low = min(adj_vertex.low, vertex.low)

        if vertex.parent.low < vertex.low:
            self.output.append((vertex, vertex.parent))

        return vertex.low

    def _adjacent_edges(self, vertex: Vertex) -> List[Vertex]:
        """
        :param vertex:
        :return: list of vertices which are adjacent of given "vertex"
        """
        return self.edges.get(vertex) or []

    @property
    def _next_id(self) -> int:
        """
        :return: next generated number which is greater than previously
                 generated number
        """
        return next(self._counter)

    @cached_property
    def _counter(self) -> count:
        return count()

    @cached_property
    def output(self) -> List[Tuple[Vertex, Vertex]]:
        """
        :return: list of edges which are critical connection
        """
        return []


def get_cc(vertices: List[Hashable], edges: Dict[Hashable, List[Hashable]]) -> List[Tuple[Hashable, Hashable]]:
    """
    :param vertices: list of hashable entities such as int, string, float etc
    :param edges: mapping of vertex to neighboring vertices
    :return: list of tuple and each tuple is of size 2, representing an CC edge by two adjacent vertices
    """
    vs = {v: Vertex(id=v) for v in vertices}
    es = {vs[v]: [vs[adj_vertex] for adj_vertex in adjacent_vertices] for v, adjacent_vertices in edges.items()}

    output = CriticalConnection(vertices=list(vs.values()), edges=es).process()

    return [(a.id, b.id) for a, b in output]


if __name__ == '__main__':
    connections = {
        'A': ['B', 'C'],
        'B': ['A', 'C'],
        'C': ['A', 'B', 'D'],
        'D': ['C', 'E', 'F'],
        'E': ['D', 'F'],
        'F': ['D', 'E']
    }
    print(get_cc(list(connections), connections))
