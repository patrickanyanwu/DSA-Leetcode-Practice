"""
    Use a heap to keep track of the nth maximum numbers,
    use a seen set to avoid adding duplicate numbers to the heap.
    If the length of seen is < 3 meaning there is less than 3 distinct numbers
    we return the max number from nums as expected.
    I then remove from the heap 3 times to get the third maximum number.
    O(n log n) time O(n) space
"""

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        seen = set()
        heap = []

        for num in nums:
            if num in seen:
                continue
            seen.add(num)
            heappush(heap, -num)

        if len(seen) < 3:
            return max(nums)
            
        for i in range(3):
            if len(heap):
                res = -heappop(heap)
        return res
