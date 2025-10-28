"""
I used backtracking to generate all valid
combinations. I tracked the count of open
and close parentheses, only adding a close
parenthesis when there were more opens, and
stopping when both counts reached n.
O(4^n / sqrt(n)) time O(n) space
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(num_open, num_close, s):
            if num_open > n or num_close > n:
                return
            if num_open == num_close == n:
                res.append(s)
                return
            if num_open < n:
                backtrack(num_open + 1, num_close, s + "(")
            if num_close < n:
                if num_open > num_close:
                    backtrack(num_open, num_close + 1, s + ")")
        backtrack(0, 0, "")
        return res