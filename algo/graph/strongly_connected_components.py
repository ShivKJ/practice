from collections import defaultdict
from dataclasses import dataclass
from functools import cached_property
from typing import Dict, Hashable, List, Set


@dataclass
class SCC:
    """
    finding strongly connected components
    """
    vertices: List[Hashable]
    edges: Dict[Hashable, List[Hashable]]

    def process(self) -> List[Set[Hashable]]:
        """
        :return:
        """
        self._first_pass_dfs()
        return self._second_pass_dfs()

    def _second_pass_dfs(self) -> List[Set[Hashable]]:
        """
        :return:
        """
        visited_vertices = set()
        visited_before_current_vertex_dfs = set()
        output = []

        for vertex in reversed(self.stack):
            self._dps(vertex, visited_vertices, is_first_pass_dfs=False)

            new_visited_vertices = visited_vertices - visited_before_current_vertex_dfs

            if new_visited_vertices:
                output.append(new_visited_vertices)
                visited_before_current_vertex_dfs.update(new_visited_vertices)

        return output

    def _first_pass_dfs(self):
        """
        :return:
        """
        visited_vertices = set()

        for vertex_index in self.vertices:
            self._dps(vertex_index, visited_vertices)

    def _dps(self, vertex: Hashable, visited_vertices: Set[Hashable], is_first_pass_dfs=True):
        """
        :param vertex:
        :param visited_vertices:
        :param is_first_pass_dfs:
        :return:
        """
        if vertex in visited_vertices:
            return

        visited_vertices.add(vertex)

        for adj_vertex in self.adjacent_vertices(vertex, reverse_edge=not is_first_pass_dfs):
            self._dps(adj_vertex, visited_vertices, is_first_pass_dfs=is_first_pass_dfs)

        if is_first_pass_dfs:
            self.stack.append(vertex)

    def adjacent_vertices(self, vertex: Hashable, reverse_edge=False) -> Set[Hashable]:
        """
        :param vertex:
        :param reverse_edge:
        :return:
        """
        edges = self.reversed_edges if reverse_edge else self.edges
        return edges.get(vertex) or frozenset()

    @cached_property
    def stack(self) -> List[Hashable]:
        """
        :return:
        """
        return []

    @cached_property
    def reversed_edges(self) -> Dict[Hashable, Set[Hashable]]:
        """
        :return:
        """
        output = defaultdict(list)

        for vertex, adjacent_vertices in self.edges.items():
            for adj_vertex in adjacent_vertices:
                output[adj_vertex].append(vertex)

        return dict(output)
