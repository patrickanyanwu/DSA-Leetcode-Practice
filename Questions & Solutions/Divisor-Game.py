"""
    When I first looked at the Divisor Game problem, I tried to think about small examples to spot a pattern.
    If n = 1, Alice can’t move, so she loses. If n = 2, she can subtract 1 and win. For n = 3, 
    whatever Alice does gives Bob a winning position. 
    I noticed that every even number lets Alice force an odd number onto Bob, 
    and every odd number forces an even number onto Alice. 
    That means Alice always wins when n is even and loses when it’s odd. So instead of simulating the game,
    I realized I can just check if n is even which is simply return not n % 2.
    O(1) time and space.
"""

class Solution:
    def divisorGame(self, n: int) -> bool:
        return not n % 2