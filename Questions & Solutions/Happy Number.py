"""I have a seen set for each new sum found and run a loop while we have not found it to be happy or unhappy,
we use a seen set as if it is not happy it will end up looping endlessly and will eventually go to a number that has already been found.
O(logn) time O(logn) space."""

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))
        return n == 1
