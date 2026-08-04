"""
  convert prerequisites into an adjacency list with the edges being what courses need to be completed in order for that course to be completed.
  I then initialize a visit set to catch circular dependencies. W e now run dfs through each node in the adjaceny list and
  if we hit a node that has no dependencies we return True or if we finished our search with no false returns we set that nodes edjelist to be empty to mark it as (can be completed)
  we then remove the node from our visit set.
  If we ever hit a node that has already been visited in the current path we return False as we found a circular dependency.
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        adj = {i: [] for i in range(numCourses)}
        for res, cur in prerequisites:
            adj[res].append(cur)
        visit = set()
        def dfs(cur):
            if cur in visit:
                return False
            if adj[cur] == []:
                return True
            visit.add(cur)
            for v in adj[cur]:
                if not dfs(v):
                    return False
            visit.remove(cur)
            adj[cur] = []
            return True
        for i in range(numCourses):
            if i in adj:
                if not dfs(i):
                    return False
        return True
