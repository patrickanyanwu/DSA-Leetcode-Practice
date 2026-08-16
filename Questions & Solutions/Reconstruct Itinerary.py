"""
  This is an Eulerian path problem (visit every ticket/edge exactly once),
  solved with Hierholzer's algorithm.

  Build an adjacency list mapping each airport to its destinations. Sort all
  tickets first and insert them in reverse order, so each destination list
  ends up sorted in *reverse* alphabetical order. That way, popping from the
  end of the list (an O(1) operation) always gives us the lexicographically
  smallest next destination, which is what greedy itinerary selection needs.

  Run a DFS from 'JFK': at each airport, keep consuming (popping) outgoing
  tickets and recursing into them until the current airport has no tickets
  left, then append it to res. This backtracks correctly even when a greedy
  choice leads down a dead end, because a node only gets appended to res once
  all of its edges are exhausted - so the last airports to get "stuck" (no
  more outgoing tickets) are added first.

  Since res is built in reverse completion order, reverse it at the end to
  get the correct itinerary. O(E log E) time (dominated by the sort) and
  O(E) space for the adjacency list and recursion stack.
"""

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)

        res = []
        def dfs(src):
            while adj[src]:
                dst = adj[src].pop()
                dfs(dst)
            res.append(src)

        dfs('JFK')
        return res[::-1]