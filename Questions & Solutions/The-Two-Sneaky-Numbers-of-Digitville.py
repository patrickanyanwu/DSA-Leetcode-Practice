"""
    I used XOR to find the two duplicates. I
    XORed all numbers and their expected values
    to isolate the duplicates, then used a
    differentiating bit to separate them into
    two groups and XOR each group separately.
    O(n) time O(1) space
"""

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        x = 0
        for num in nums:
            x ^= num
        for i in range(len(nums) - 2):
            x ^= i

        diff_bit = x & -x
        xor1 = xor2 = 0

        for num in nums:
            if num & diff_bit:
                xor1 ^= num
            else:
                xor2 ^= num

        for i in range(len(nums) - 2):
            if i & diff_bit:
                xor1 ^= i
            else:
                xor2 ^= i
                
        return [xor1, xor2]