from algo.graph.strongly_connected_components import SCC

if __name__ == '__main__':
    edge_mapping = {
        'A': ['B'],
        'B': ['C'],
        'C': ['A', 'D']

        # 'B': ['C', 'D'],
        # 'A': ['B'],
        # 'C': ['A'],
        # 'D': ['E'],
        # 'E': ['F'],
        # 'F': ['D'],
        # 'K': [],
        # 'I': ['J'],
        # 'H': ['I'],
        # 'G': ['F', 'H'],
        # 'J': ['K', 'G'],
    }

    vertices = list(edge_mapping)
    vertices.sort()

    print(SCC(vertices=vertices, edges=edge_mapping).process())
