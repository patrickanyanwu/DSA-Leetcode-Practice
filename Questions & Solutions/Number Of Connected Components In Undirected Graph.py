"""
  Union-Find (Disjoint Set Union) approach: start by assuming every node is its
  own component, so res = n. Each node is its own parent initially.

  For every edge (u, v), try to union the sets containing u and v:
    - find() walks up to each node's root parent, compressing the path along
      the way so future lookups are near O(1).
    - if u and v already share a root, they're already in the same component,
      so the edge is redundant and res stays the same.
    - otherwise we merge the two sets (attaching the smaller-rank tree under
      the larger one to keep the trees shallow) and decrement res by 1, since
      two components just became one.

  After processing all edges, res holds the final number of connected
  components. With path compression + union by rank this runs in
  O(V + E * α(n)) time (V for the initial parent/rank setup, effectively
  linear thereafter) and O(V) space.
"""

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = n
        rank = [0] * n
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(u, v):
            parentU, parentV = find(u), find(v)
            if parentU == parentV:
                return False
            if rank[parentU] < rank[parentV]:
                parentU, parentV = parentV, parentU
            parent[parentV] = parentU

            if rank[parentU] == rank[parentV]:
                rank[parentU] += 1

            return True
            
        for u, v in edges:
            if union(u, v):
                res -= 1

        return res
