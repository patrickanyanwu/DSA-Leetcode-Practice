class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        I used bit manipulation to find the single number that appears once
        while others appear three times. For each of the 32 bits, I count how
        many numbers have that bit set. If the count is not divisible by 3,
        it means the single number has that bit set, so I add it to my result
        using bitwise OR. After processing all bits, I handle the negative
        number case by checking if the result is >= 2^31, then converting it
        to a signed 32-bit integer by subtracting 2^32. This works because
        bits appearing 3 times cancel out modulo 3.
        O(32n) = O(n) time O(1) space
        """
        result = 0
        for bit in range(32):
            bit_count = 0
            for num in nums:
                if (num >> bit) & 1:
                    bit_count += 1
            if bit_count % 3:
                result |= (1 << bit)
        
        if result >= 2**31:
            result -= 2**32
        return result