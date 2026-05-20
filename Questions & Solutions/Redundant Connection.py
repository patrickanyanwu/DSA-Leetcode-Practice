"""
Use Union-Find to detect the first edge that creates a cycle.
Initialize each node as its own parent with rank 1.
For each edge, find the roots of both nodes using path compression (par[p] = par[par[p]] flattens the tree on the way up).
If both nodes share the same root, they are already connected — this edge is redundant, return it immediately.
Otherwise, union the two components by attaching the smaller-rank root under the larger one (union by rank) to keep the tree flat.
O(n * α(n)) time where α is the inverse Ackermann function (effectively constant), O(n) space for the parent and rank arrays.
"""

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]