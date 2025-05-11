"""
  Sort the potions so we can run binary search on them,
  for each spell we run binary search on the potions to try and find the smallest index where the product is >= success.
  we then apppend to our result the length of potions - the smallest index found (gives the number of pairs that are succesful).
  O(m log n) time O(m) space, where m is number of spells and n is number of potions.
"""

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        potions = sorted(potions)
        n = len(potions)
        for spell in spells:
            l, r = 0, n - 1
            count = 0
            idx = n
            while l <= r:
                m = l + ((r - l) // 2)
                summ = spell * potions[m]
                if summ < success:
                    l = m + 1
                else:
                    idx = m
                    r = m - 1
            res.append(n - idx)
        return res
