class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        """
        I used a min heap to efficiently find k pairs with smallest sums. I
        start by pushing the first k elements from nums1 paired with nums2[0]
        into the heap, since these are guaranteed to be among the smallest. For
        each iteration, I pop the smallest sum pair and add it to results. Then
        I push the next pair from the same nums1 element paired with the next
        nums2 element (j+1) if it exists. This ensures I explore pairs in
        increasing order of sums without generating all possible pairs. I limit
        initial heap size to min(k, len(nums1)) to avoid unnecessary work.
        O(k log k) time O(k) space
        """
        if not nums1 or not nums2 or k == 0:
            return []
            
        minheap = []
        res = []
        
        for i in range(min(k, len(nums1))):
            heappush(minheap, (nums1[i] + nums2[0], i, 0))
        
        while k > 0 and minheap:
            s, i, j = heappop(minheap)
            res.append([nums1[i], nums2[j]])
            
            if j + 1 < len(nums2):
                heappush(minheap, (nums1[i] + nums2[j+1], i, j+1))
            
            k -= 1
        
        return res