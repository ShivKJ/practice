from typing import Dict, List


def no_cycle(vertices: int, edges: Dict[int, List[int]]) -> bool:
    """
    :param vertices: total number of vertices in the graph
    :param edges: mapping of vertex to adjacent vertices
    :return: True if there is no cycle in graph represented by vertices and edges
    """
    visited = ['NEW'] * vertices

    for vertex in range(vertices):
        if visited[vertex] == 'NEW':
            if not dfs(vertex, edges, visited):
                # if there is a cycle then returning False
                return False

    return True


def dfs(vertex: int, edges: Dict[int, List[int]], visited: List[str]) -> bool:
    """
    :param vertex: vertex on which DFS is called
    :param edges: mapping of vertex to adjacent vertices
    :param visited: list of string having three values
                    1) NEW (if vertex has not been visited before)
                    2) ACTIVE (if vertex is in DFS-stack)
                    3) FINISHED (if vertex is out of DFS-stack)
    :return: True if this vertex is not part of any cycle
    """
    visited[vertex] = 'ACTIVE'

    for adjacent_vertex in edges.get(vertex) or []:
        if visited[adjacent_vertex] == 'ACTIVE':
            # it means there is a path from adjacent vertex to this vertex
            return False
        elif not dfs(adjacent_vertex, edges, visited):
            return False

    visited[vertex] = 'FINISHED'

    return True
