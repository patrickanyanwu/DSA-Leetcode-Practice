"""Use a hasmap with key being the number and the gvalue being its most recent index, now for each number if it is not already in the hashmap we add it and its index.
If the number is in the hasmap (we have a duplicate) we check if the index difference is less than or equal to k, if so we return false,
if not we update the index of that number top the current index and continue. If a valid duplicate is not found the loop will finish and we return false.
O(n) time and O(n) space."""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hasht = {}
        for i, num in enumerate(nums):
            if num not in hasht:
                hasht[num] = i
            else:
                if abs(hasht[num] - i) <= k:
                    return True
                hasht[num] = i
        return False
