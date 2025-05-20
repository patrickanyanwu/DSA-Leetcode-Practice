"""
  Run counting sort on the citations,
  we then loop backwards in the count array and keep track of the amount of papers we have by
  incrementing it by the amount of papers for the current count.
  As soon as the amount of papers we have is >= to our h index we return that h
  O(n) time O(1) sapce.
"""

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        count = [0] * (n + 1)

        for c in citations:
            count[min(c, n)] += 1
        h = n
        papers = count[n]
        while papers < h:
            h -= 1
            papers += count[h]
        return h
