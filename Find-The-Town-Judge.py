"""
  Convert trust list to a graph using an adjacency list, i then use sets to check which nodes had an edge going to them but but has edges itself.
  if we have more than one in tha case or we have zero we return -1 immediatly as there is no town judge. Now we check if that lonely node is in every other nodes edges.
  If it is we return true and if not we return false.
  O(n) time O(n) space.
"""

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust and n == 1:
            return 1
        adjlist = defaultdict(set)
        none = set()
        others = set()
        for u, v in trust:
            adjlist[u].add(v)
            none.add(u)
            others.add(v)
        lonely = others - none
        if not lonely or len(lonely) > 1:
            return -1
        lone = list(lonely)[0]
        count = 0
        for u, edges in adjlist.items():
            if lone in edges:
                count += 1
        return lone if count == n - 1 else -1
