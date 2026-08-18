from collections import defaultdict

def kosaraju_scc(n, edges):
    # Step 1: Build original graph
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    # Step 1: DFS on original graph, track finish order
    visited = [False] * n
    finish_stack = []

    def dfs1(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs1(neighbor)
        finish_stack.append(node)  # post-order: append AFTER exploring all neighbors

    for node in range(n):
        if not visited[node]:
            dfs1(node)

    # Step 2: Build transposed graph (reverse every edge)
    reverse_graph = defaultdict(list)
    for u, v in edges:
        reverse_graph[v].append(u)

    # Step 3: DFS on transposed graph, in reverse finish order
    visited = [False] * n
    sccs = []

    def dfs2(node, component):
        visited[node] = True
        component.append(node)
        for neighbor in reverse_graph[node]:
            if not visited[neighbor]:
                dfs2(neighbor, component)

    while finish_stack:
        node = finish_stack.pop()
        if not visited[node]:
            component = []
            dfs2(node, component)
            sccs.append(component)

    return sccs