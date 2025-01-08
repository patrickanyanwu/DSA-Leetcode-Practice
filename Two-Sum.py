"""Use the enumerate function to put each number in the array into a HashMap with the key being the number and the value being its index.
Then for every number in the input array, I check if the target – number is in the set and the index of target - number is not equal to the index of the current number,
if these statements are true then return both indexes. O(n) time O(n) space"""





class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}  # value -> index

        for i, n in enumerate(nums):
            indices[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
