"""
  Create a hashmap with the key being the number and the value being its characters in the phone,
  we now initialize 2 arrays, res is our result array and sol is our current solution array.
  Now we make a backtrack function and what it does is it starts at index 0 in digits,
  for each letter in the corresponding digits characters we add it to our result and call the function on the next index to explore the next option.
  After we finish exploring all options with that specific character we backtrack by popping it off the sol and chosing another character.
  O(n * m ^ n), O(n * m ^ n) space. 
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        combs = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res, sol = [], []
        def backtrack(i):
            if len(sol) == len(digits):
                res.append("".join(sol))
                return
            for char in combs[digits[i]]:
                sol.append(char)
                backtrack(i + 1)
                sol.pop()
        backtrack(0)
        return res
