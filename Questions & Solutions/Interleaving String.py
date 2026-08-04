class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        I used dynamic programming to check if s3 can be formed by interleaving
        s1 and s2. I first verify lengths match, returning False if not. I
        create a 2D DP table where dp[i][j] represents whether the first i
        characters of s1 and first j characters of s2 can form the first i+j
        characters of s3. I initialize dp[0][0] to True as empty strings
        interleave to empty. For each position, I check if taking a character
        from s1 (if it matches s3[i+j-1]) or from s2 (if it matches) leads to a
        valid interleaving. The answer is at dp[n][m].
        O(n × m) time O(n × m) space
        """
        n, m = len(s1), len(s2)
        if n + m != len(s3):
            return False

        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True

        for i in range(n + 1):
            for j in range(m + 1):
                if i > 0 and dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]:
                    dp[i][j] = True
                if j > 0 and dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] = True

        return dp[n][m]