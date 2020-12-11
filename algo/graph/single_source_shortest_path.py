from dataclasses import dataclass, field
from math import inf
from typing import Dict, Hashable, List, Tuple


@dataclass
class Vertex:
    """
    vertex of graph
    """
    id: Hashable  # id of this vertex

    # if there is a path from desired vertex to this vertex, then this will be the
    # parent node of this vertex
    parent: 'Vertex' = field(default=None, init=False, compare=False)
    distance: float = field(default=inf, init=False, compare=False)  # distance from desired source vertex
    pq_index: int = field(default=None, init=False)  # index of this vertex in adaptable-pq array

    def __str__(self):
        return f'Vertex(id={self.id}, distance={self.distance}, parent={self.parent.id})'

    def __repr__(self):
        return str(self)


@dataclass
class PQ:
    """
    Impl of adaptable min-priority queue. It implements the following methods
    1) pop (deleting element with least priority(distance))
    2) update (updating priority of an element)
    3) is_empty (checks if there is no element in queue)
    """
    arr: List[Vertex]  # all the vertices used in dijkstra algorithm
    size: int = field(init=False)  # available nodes in arr

    def __post_init__(self):
        self.size = len(self.arr)
        self._heapify()

    def update(self, v: Vertex, distance: float):
        """
        updating priority (distance) of vertex
        :param v:
        :param distance:
        """
        v.distance = distance
        bubbled_down = self._bubble_down(v.pq_index)

        if not bubbled_down:
            self._bubble_up(v.pq_index)

    def pop(self) -> Vertex:
        """
        :return: element with least priority (distance)
        """
        if self.is_empty:
            raise ValueError(f'no element in PQ')

        arr = self.arr
        self.size -= 1

        output = arr[0]
        arr[0], arr[self.size] = arr[self.size], None

        self._bubble_down(0)

        return output

    @property
    def is_empty(self) -> bool:
        """
        :return: True if there is no element available in the queue
        """
        return self.size == 0

    def __bool__(self):
        """
        :return: True if there are some element in the queue
        """
        return not self.is_empty

    def _heapify(self):
        """
        creating min heap on "arr".
        """
        for i in reversed(range(self.size)):
            v = self.arr[i]
            v.pq_index = i
            self._bubble_down(i)

    def _bubble_up(self, child: int):
        """
        :param child:
        :return:
        """
        arr = self.arr

        while child != 0:  # child is not root node
            parent = self._parent(child)

            if arr[parent].distance > arr[child].distance:
                self._swap(parent, child)
                child = parent
            else:
                break

    def _bubble_down(self, parent) -> bool:
        """
        :param parent:
        :return: True if child nodes have lesser priority than parent node
        """
        smallest = parent
        left_child = self._left(parent)

        if left_child < self.size and self.is_greater(smallest, left_child):
            left_child = smallest

        right_child = left_child + 1

        if right_child < self.size and self.is_greater(smallest, right_child):
            smallest = right_child

        if smallest != parent:
            self._swap(parent, smallest)
            self._bubble_down(smallest)

            return True

        return False

    def is_greater(self, u: int, v: int) -> bool:
        """
        :param u:
        :param v:
        :return: True if vertex represented by uth index has high priority than that of vth index
        """
        return self.arr[u].distance > self.arr[v].distance

    def _swap(self, i: int, j: int):
        """
        swapping ith and jth vertices in the queue
        :param i:
        :param j:
        """
        arr = self.arr

        arr[i].pq_index = j
        arr[j].pq_index = i

        arr[i], arr[j] = arr[j], arr[i]

    @staticmethod
    def _left(parent: int) -> int:
        """
        :param parent: left child of given parent
        :return:
        """
        return 2 * parent + 1

    @staticmethod
    def _parent(child) -> int:
        """
        :param child:
        :return:
        """
        return (child - 1) // 2


def validate_edge_weight(edges: Dict[Hashable, List[Tuple[Hashable, float]]]):
    """
    :param edges: mapping from a vertex (say A) to list of tuple of size 2.
                  First element is adjacent vertex (say B) and second is edge-distance
                  from the A to B
                  raising exception if the edge-distance is negative.
    """
    for u, adjacent_edges in edges.items():
        for v, distance in adjacent_edges:
            if distance < 0:
                raise ValueError(f'edge=({u},{v}) has negative weight ({distance})')


def shortest_path_dijkstra(vertices: List[Hashable], edges: Dict[Hashable, List[Tuple[Hashable, float]]],
                           source: Hashable) -> Dict[Hashable, Vertex]:
    """
    :param vertices:
    :param edges: mapping from a vertex (say A) to list of tuple of size 2.
                  First element is adjacent vertex (say B) and second is edge-distance
                  from the A to B.

                  NOTE: all the edge-distance must be non-negative

    :param source: distance from this vertex to all the other vertices are calculated
    :return: mapping from vertex-id to vertex object. Vertex object contains the following attribute
            1) distance from given "source" vertex
            2) if the vertex is reachable from "source" vertex then parent vertex which will be
               visited from "source" vertex which is visited just before
    """
    validate_edge_weight(edges)

    vertex_id_to_obj = {i: Vertex(id=i) for i in vertices}

    source_vertex = vertex_id_to_obj[source]

    source_vertex.distance = 0  # distance from source vertex to same vertex is 0
    source_vertex.parent = source_vertex  # setting parent of source vertex to itself so as to
    # distance those vertices which are not reachable from source vertex. If a vertex is not
    # reachable from source vertex then parent attribute is None

    processed_vertex_id = set()

    pq = PQ(list(vertex_id_to_obj.values()))

    while pq:
        u = pq.pop()
        processed_vertex_id.add(u.id)

        for v_id, distance in edges.get(u.id) or []:
            v = vertex_id_to_obj[v_id]

            if v_id not in processed_vertex_id:
                relaxed_distance = u.distance + distance

                if v.distance > relaxed_distance:
                    v.parent = u
                    pq.update(v, relaxed_distance)

    return vertex_id_to_obj


# def relax(u: Vertex, v: Vertex, edge_distance: float) -> bool:
#     """
#     :param u:
#     :param v:
#     :param edge_distance:
#     :return: True if v.distance is updated using u.distance and edge distance
#     """
#     if v.distance > u.distance + edge_distance:
#         v.distance = u.distance + edge_distance
#         v.parent = u
#         return True
#
#     return False
#
#
# def bellman_ford(vertices: List[Hashable], edges: Dict[Tuple[Hashable, Hashable], float], src: Hashable):
#     vertices = {v: Vertex(id=v) for v in vertices}
#
#     src = Vertex(id=src)
#     src.distance = 0
#     src.parent = src
#
#     for i in range(len(vertices) - 1):
#         for (u, v), w in edges.items():
#             relax(vertices[u], vertices[v], w)
#
#     for (u, v), w in edges.items():
#         if vertices[v].distance > vertices[u].distance + w:
#             return False
#
#     return True
#

if __name__ == '__main__':
    vertex_distance = shortest_path_dijkstra(list(range(1, 8)), {
        1: [(2, 6), (4, 16), (3, 2)],
        2: [(5, 4), (4, 5)],
        3: [(2, 7), (5, 3), (6, 8)],
        4: [(7, 3)],
        5: [(4, 4), (7, 10)],
        6: [(7, 1)],
        7: []
    }, 1)
    print(vertex_distance)
