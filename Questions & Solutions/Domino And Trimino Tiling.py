"""
  A complete 2×n tiling can be formed by adding a vertical domino to any 2×(n−1) tiling,
  appending one of two mirrored L-shaped tromino hooks to any 2×(n−1) tiling (yielding 2·dp[n−1]),
  or filling the final three columns entirely with a complementary pair of trominoes (dp[n−3]) ensuring complete coverage with no overlaps.
  O(n) time O(1) space.
"""

class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2
        a, b, c = 1, 1, 2
        for _ in range(3, n+1):
            a, b, c = b, c, (2*c + a) % MOD
        return c
