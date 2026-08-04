"""We set 2 pointers at the second index because we are going to be checking the previous values of r, so we have these checks: if numr r is equal to nums r - 1 we only increment r, 
if nums at r is not equal to the number before it we know we have found a new distinct number so we set nums at l to that number.
After all of that we loop through the array from the position where l was left and we set the number at each index equal to an underscore as they are duplicates.
We then return l as that is automatically the number of distinct elements in the array.
O(n) time O(1) space."""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = r = 1
        while r < len(nums):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
            r += 1
        for j in range(l, len(nums)):
            nums[j] = "_"
        return l
