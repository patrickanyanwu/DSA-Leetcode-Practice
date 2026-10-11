"""
Use Floyd's cycle detection (slow/fast pointers) where "moving forward" means applying the sum-of-squared-digits transformation.
If a number is happy, repeatedly applying this transformation eventually reaches 1; if it's not happy, the sequence enters a cycle that never includes 1.
Start fast two steps ahead of slow, then advance fast by two transformations and slow by one each iteration — if there's a cycle, they're guaranteed to meet (slow == fast) just like in linked-list cycle detection.
Once they meet, check whether that meeting value is 1: if so the number is happy, otherwise it's stuck in a non-1 cycle.
O(log n) time per transformation and a bounded number of iterations before a cycle is found, O(1) space since no set of seen values is stored.
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sumOfSquares(n)

        while slow != fast:
            fast = self.sumOfSquares(fast)
            fast = self.sumOfSquares(fast)
            slow = self.sumOfSquares(slow)
        return True if fast == 1 else False

    def sumOfSquares(self, n: int) -> int:
        output = 0

        while n != 0:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10
        return output