"""
  Use recursive backtracking with memoization, for each word we chose we can chose any other word in the worddict. We only chose a word if it is valid,
  we check that useing string indexing. We return True if the current word is equal to our input string.
  O(n * m * k) time O(n) space n is length of input string, m is amount of words in worddict, k is length of longest word in worddict. 
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        res = [False]
        memo = {}
        def backtrack(word):
            if word in memo:
                return memo[word]
            if word == s:
                return True
            if len(word) >= len(s):
                return False
            for cur in wordDict:
                if s[:len(word + cur)] == word + cur:
                    if backtrack(word + cur):
                        res[0] = True
                        memo[word] = True
                        return
                    else:
                        memo[word] = False
        backtrack("")
        return res[0]
