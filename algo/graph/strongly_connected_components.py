from collections import defaultdict
from dataclasses import dataclass
from functools import cached_property
from typing import Dict, Hashable, Iterable, List, Set


@dataclass
class SCC:
    """
    finding strongly connected components (SCC)

    SCC is set of vertices of a directed graph such that all of them are
    reachable from each other. Number of vertices in a SCC can not be increased

    In the implementation, we find all the SCC of directed graph
    """
    vertices: List[Hashable]  # all the vertices much be hashable like int, float, str, uuid etc

    # key of this dict is a vertex and vertices connected through outgoing edges
    edges: Dict[Hashable, List[Hashable]]

    def process(self) -> List[Set[Hashable]]:
        """
        To create SCC, we use DFS twice in the following ways
        1) First DFS is used to find finishing time of each vertices in the traversal
        2) Then we reverse the edges and DFS is run. However vertex which will work as source vertex in DFS
           is prioritised on the basis of its finishing time in first DFS
        :return: list of set and each each set of vertices which form one SCC
        """
        self._first_pass_dfs()
        return self._second_pass_dfs()

    def _second_pass_dfs(self) -> List[Set[Hashable]]:
        """
        :return: list of set and each set represents one SCC
        """
        visited_vertices = set()
        visited_before_current_vertex_dfs = set()
        output = []

        for vertex in self._stack_traversal:
            self._dfs(vertex, visited_vertices, is_first_pass_dfs=False)

            new_visited_vertices = visited_vertices - visited_before_current_vertex_dfs

            if new_visited_vertices:
                output.append(new_visited_vertices)
                visited_before_current_vertex_dfs.update(new_visited_vertices)

        return output

    def _first_pass_dfs(self):
        """
        running DFS and adding vertices in stack on the basis of finishing time. Vertex with more finishing time will
        be on top of stack
        """
        visited_vertices = set()

        for vertex_index in self.vertices:
            self._dfs(vertex_index, visited_vertices)

    def _dfs(self, vertex: Hashable, visited_vertices: Set[Hashable], is_first_pass_dfs=True):
        """
        :param vertex:
        :param visited_vertices: all the vertices which have been visited before "vertex"
        :param is_first_pass_dfs: if True then given input edges are considered to find
                                  neighbors else edges are revered before running DFS
        """
        if vertex in visited_vertices:
            return

        visited_vertices.add(vertex)

        for adj_vertex in self._adjacent_vertices(vertex, reverse_edge=not is_first_pass_dfs):
            self._dfs(adj_vertex, visited_vertices, is_first_pass_dfs=is_first_pass_dfs)

        if is_first_pass_dfs:
            self._push_to_stack(vertex)

    def _adjacent_vertices(self, vertex: Hashable, reverse_edge=False) -> List[Hashable]:
        """
        :param vertex:
        :param reverse_edge:
        :return: all the vertices which are connected through outgoing edge from "vertex" if reverse_edge=False,
                 otherwise edges are reversed in the direction and then vertices connected to "vertex" through incoming
                 edges are returned
        """
        edges = self._reversed_edges if reverse_edge else self.edges
        return edges.get(vertex) or []

    @cached_property
    def _reversed_edges(self) -> Dict[Hashable, List[Hashable]]:
        """
        :return: reversing edges represented by "self.edges" and returning it
        """
        output = defaultdict(list)

        for vertex, adjacent_vertices in self.edges.items():
            for adj_vertex in adjacent_vertices:
                output[adj_vertex].append(vertex)

        return dict(output)

    @cached_property
    def _stack(self) -> List[Hashable]:
        """
        :return: a list which will be used to store the order in which
                 vertices are visited in First DFS traversal
        """
        return []

    @property
    def _stack_traversal(self) -> Iterable[Hashable]:
        """
        since stack used in the impl is created from list, reversing the order of list
        to equivalently traverse the stack
        :return:
        """
        return reversed(self._stack)

    def _push_to_stack(self, vertex: Hashable):
        """
        since stack is impl through a list, adding vertex to end of list and to find the
        top element of stack, last element of stack can be checked
        :param vertex:
        """
        self._stack.append(vertex)
