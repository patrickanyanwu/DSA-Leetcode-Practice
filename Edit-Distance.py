"""
  We run a dfs and for each index we eather replace the character from word1, delete from word1 or insert the charcter from word2.
  This is done with indexes that only move based on conditions and we return the minimum of all results.
  If i = len(word1) we return the amount of characters we had left in the other word as that is the amount of deletions we need to make
  and the same for j and len word2.
  If the letters are equal we dont increase our count we just continue the dfs.
  Memoize results with a cache.
  O(m * n) time O(m * n) space.
"""

from functools import lru_cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        @lru_cache(None)
        def dfs(i: int, j: int) -> int:
            if i == m:
                return n - j
            if j == n:
                return m - i
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
                
            replace = 1 + dfs(i + 1, j + 1)
            delete  = 1 + dfs(i + 1, j)
            insert  = 1 + dfs(i, j + 1)

            return min(replace, delete, insert)

        return dfs(0, 0)
