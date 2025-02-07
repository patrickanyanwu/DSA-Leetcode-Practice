"""We set variables i, j and k equal to infinity.
Now as we iterate through we check each number against i, j and k so if the number is less than i we set i to that number so when we find a number less than the new I we change our i again.
And for if the number is greater than i we check against j and we also check agais k. This algorithm allows for it to check orderly and update accordingly in linear time and no extra space.
O(n) time, O(1) space"""

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i = j = k = float("inf")

        for num in nums:
            if num <= i:
                i = num
                continue
            if num <= j:
                j = num
                continue
            if num <= k:
                k = num
        if i != float("inf") and j != float("inf") and k != float("inf"):
            return True
        return False
