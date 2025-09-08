"""We work backwards with a pointer at the end of the nums1 array, we then make our checks, 
if the number at nums1[m] is greater than the number at nums2[n] we know we have to put that number at the end (nums1[last])
we then decrement m to compare against the next number. After every check our last pointer decrements to find the next appropriate position.
After we check if we still have numbers to add from nums2 if so we make the appropriate swaps.
O(n) time O(1) space.
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        last = m + n - 1

        while n > 0 and m > 0:
            if nums1[m - 1] < nums2[n - 1]:
                nums1[last] = nums2[n - 1]
                n -= 1
            else:
                nums1[last] = nums1[m - 1]
                m -= 1
            last -= 1
        
        while n > 0:
            nums1[last] = nums2[n - 1]
            last -= 1
            n -= 1
