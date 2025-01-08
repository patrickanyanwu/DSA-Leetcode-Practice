""" Used bucket sort algorithm, used hashmap with key is number and value is its frequency in the array.
We then made our bucket which is a list of lists with its indexes going 1 more than the length of the input array so it accounts for when the entire list is the same number.
We add each number to our bucket (count) with its index in the bucket being its frequency in the input array.
We then work backward from the end of the bucket and append each number to a result array, after every append in our bucket[i] we check if the length of our results equal to k and if so we return result. 
O(n) time O(n) space"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hasht = defaultdict(int)
        count = [[] for i in range(len(nums) + 1)]
        for num in nums:
            hasht[num] += 1
        for c, n in hasht.items():
            count[n].append(c)
        res = []
        for i in range(len(nums), 0, -1):
            for n in count[i]:
                res.append(n)
                if len(res) == k:
                    return res
