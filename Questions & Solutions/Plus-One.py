"""
I traversed the digits from right to left,
incrementing the first digit less than 9
and returning immediately. If all digits
were 9, I set them to 0 and prepended a 1
to handle the carry.
O(n) time O(1) space
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        
        return [1] + digits