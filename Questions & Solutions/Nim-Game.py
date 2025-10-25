"""
    If we ever have an n thats a multiple of 4
    no matter how many we take each time the opponent will win
    take for example n = 4
    take 1 leave 3
    rake 2 leave 2
    take 3 leave 1
    the oppenent will always be able to take the remaining stones
"""

class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0