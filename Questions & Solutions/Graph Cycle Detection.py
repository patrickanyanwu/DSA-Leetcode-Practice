"""
Detect a cycle in a directed graph using DFS with three-color state tracking.
Build an adjacency list from the edge list.
state[node] is 0 (unvisited), 1 (in the current DFS path), or 2 (fully explored).
When DFS visits a node, mark it 1; if it reaches a neighbour already marked 1, that neighbour is an ancestor on the current path, so a cycle exists.
Unvisited neighbours (state 0) are explored recursively; once a node's neighbours are all processed with no cycle found, mark it 2 so it's never re-explored.
Run DFS from every unvisited node to cover disconnected components.
O(n + e) time since each node and edge is processed once, O(n + e) space for the adjacency list and state array.
"""

from collections import defaultdict

def graph_has_cycle(n, edges):
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)

    state = [0] * n

    def dfs(node):
        state[node] = 1

        for neighbour in graph[node]:
            if state[neighbour] == 1:
                return True
            if state[neighbour] == 0:
                if dfs(neighbour):
                    return True
                
        state[node] = 2
    for i in range(n):
        if not state[i]:
            if dfs(i):
                return True
    return False