"""Use two pointers, one at beginning and one at end. We then check our sum in the loop, if the sum is greater we decrement the right pointer to find a smaller value as the array is sorted.
If the sum is less we increment the left pointer to find a greater sum.
O(n) time O(1) space."""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            summ = numbers[l] + numbers[r]
            if summ > target:
                r -= 1
            elif summ < target:
                l += 1
            else:
                return [l+ 1, r + 1]
