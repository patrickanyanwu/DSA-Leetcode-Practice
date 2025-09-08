"""
  The max k we could have is the max number in the piles array as we need to eat all of the piles
  and the min is 1 as we cant eat any in 0 hours,
  So we run binary search on that range,
  if the sum of (all piles divided by the current k) is <= our max hours it is a valid k,
  we then search for a lower possible k and if not (the sum was greater than h) we search for a higher k that is valid.
  O(n log n) time O(1) sapce
"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        mini = float("inf")
        while l <= r:
            m = l + (r - l) // 2
            res = 0
            for p in piles:
                res += math.ceil(p / m)
            if res <= h:
                mini = min(mini, m)
                r = m - 1
            else:
                l = m + 1
        return mini
