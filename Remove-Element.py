"""Have 2 pointers, one at beginning and one at end of array, we then have these checks: if nums at r is equal to the value we replace that index with an underscore and increment our coount.
If nums at r is not equal to the value we check if nums at l is equal, if it is we set nums at l equal to nums at r in order to keep that number in the array.
 If neither of them are the value we just increment our left to find another occurence of the value.
 O(n) time O(1) space
 """

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums) - 1
        count = 0
        while l <= r:
            if nums[r] == val:
                nums[r] = "_"
                count += 1
                r -= 1
                continue
            else:
                if nums[l] == val:
                    nums[l] = nums[r]
                    nums[r] = "_"
                    count += 1
                    r -= 1
                l += 1
        k = len(nums) - count
        return k
