"""
  Generate a pairs array with each pair being the number in the other array with the same index.
  We then sort the array based onn the values of nums2's numbers in reverse order (max num first),
  Now we loop through while keeping track of a max triplet some and when we reach a valid sum of length k we update our result accordingly,
  heap is used so we keep track of the smallest element in our n1sum
  we remove whatever the smallest element in our n1sum is from our heap to maximise our n1sum.
  O(n log n) time O(n) space
"""

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = sorted([i for i in zip(nums1, nums2)], key=lambda p: p[1], reverse=True)
        heap = []
        n1sum = 0
        res = 0
        for n1, n2 in pairs:
            n1sum += n1
            heappush(heap, n1)
            if len(heap) > k:
                n1pop = heappop(heap)
                n1sum -= n1pop
            if len(heap) == k:
                res = max(res, n1sum * n2)
        return res
