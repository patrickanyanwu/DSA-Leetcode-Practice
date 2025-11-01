"""
    I used a set to track numbers I've seen as
    I traversed the array. When I encountered a
    number already in the set, I added it to
    the result and returned early once I found
    two duplicates.
    O(n) time O(n) space
"""

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen = set()
        res = []
        for num in nums:
            if num in seen:
                res.append(num)
                if len(res) == 2:
                    return res
            seen.add(num)