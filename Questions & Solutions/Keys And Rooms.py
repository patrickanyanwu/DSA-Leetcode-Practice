"""
  Generate adjacency list with key being the room and the values being what rooms we can enter if we enter the current room.
  Run a graph dfs and if we see all rooms throughout our dfs we return true else we return false.
  O(V + E) time O(V) space
"""

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        adj = {i: [] for i in range(len(rooms))}

        for i, room in enumerate(rooms):
            for j in room:
                adj[i].append(j)
        seen = set()
        def dfs(cur):
            seen.add(cur)
            for v in adj[cur]:
                if v not in seen:
                    dfs(v)
        dfs(0)
        return len(seen) == len(rooms)
