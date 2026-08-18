"""
  First check feasibility: connecting n computers requires at least n - 1
  cables (a spanning tree). If we have fewer connections than that, there
  simply aren't enough cables to reach everyone, so return -1.

  Otherwise, use Union-Find to count how many separate components the
  existing cables already form. Start assuming all n computers are isolated
  (res = n), then for every connection, union its two endpoints; each
  successful union (one that actually merges two distinct components) means
  one fewer component, so decrement res.

  Once all connections are processed, res is the number of connected
  components in the current network. Turning k separate components into one
  connected network only takes k - 1 "moves" (each move takes a redundant
  cable - guaranteed to exist since we passed the feasibility check - and
  uses it to link two components together), so the answer is res - 1.

  With path compression + union by rank this runs in O(V + E * α(n)) time
  (V for initial parent/rank setup, effectively linear thereafter) and O(V)
  space.
"""

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        res = n

        rank = [0] * n
        parent = [i for i in range(n)]

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
        
        for u, v in connections:
            if union(u, v):
                res -= 1

        return res - 1