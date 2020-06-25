def bfs(n, edges, s):
    """Given a list of edges of a graph with vertices 1 to n and a starting vertex s,
    this will explore every vertex connected to the starting vertex, breadth first."""

    edges_by_vertex = dict([(i, []) for i in range(1, n + 1)])
    for edge in edges:
        edges_by_vertex[edge[0]].append(edge[1])
        edges_by_vertex[edge[1]].append(edge[0])

    discovered = set()

    q = [s]    # queue
    discovered.add(s)
    while q:
        v = q.pop()
        for w in edges_by_vertex[v]:
            if w not in discovered:
                print('discovered {}'.format(w))
                discovered.add(w)
                q.insert(0, w)


bfs(5, [[1, 2], [1, 3], [3, 4]], 1)
