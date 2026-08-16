class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        self.n = n
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, u, v):
        parentU, parentV = self.find(u), self.find(v)
        if parentU == parentV:
            return False
        if self.rank[parentV] < self.rank[parentU]:
            parentU, parentV = parentV, parentU
        self.parent[parentU] = parentV

        if self.rank[parentV] == self.rank[parentU]:
            self.rank[parentV] += 1
        return True

def kruskals(n, edges):
    edges = sorted(edges, key=lambda x:x[2])
    dst, mst, total = DSU(n), [], 0
    for u, v, w in edges:
        if dst.union(u, v):
            mst.apped((u, v, w))
            total += w
        if len(mst) == n - 1:
            break
    return mst, total