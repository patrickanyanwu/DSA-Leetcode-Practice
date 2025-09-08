""" We sort the array first, now for each number in array we use two pointers with l being 1 after the current number and r being at the end of the array, we also use enumerate function to keep track of the index of the current number.
We then check if the sum of numbers at i, l, and r is equal to 0, if it is we append a list containing these numbers into our result.
If the sum is greater we decrease our right pointer in order to find a smaller number and if the sum is lower we increase our left pointer to find a greater number, this is done while l < r.
After every time a match is found, after appending to our result we increment our left pointer and while the number before l is equal to the number at l we increment l until the condition is false in order to avoid duplication.
After every run of the initial loop, we check if the number at i is equal to the number before i (avoid dublication) and if that’s true we continue to the next iteration of the loop. 
O(n ^2) time O(1) space."""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = num + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res
