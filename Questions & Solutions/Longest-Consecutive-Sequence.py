"""Make a set containing every number in the array (without duplicates as we dont take them into account).
For every number in the set we check if num – 1 is in the set, and if it is not then we know that is the start of a potential sequence (this eliminates extra unnecesary looping of numbers that dont start a sequence).
In this case, we use a while num + 1 in the set we increment our length of the current sequence by one and increment our current number by 1 to check again.
After the while loop is done we have a longest variable which is equal to the max between the previous longest and the current sequence in order to keep updating the max.
O(n) time O(n) space"""



class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set1 = set(nums)
        longest = 0
        for num in set1:
            if num - 1 not in set1:
                current_seq = 1
                while num + 1 in set1:
                    current_seq += 1
                    num += 1
                longest = max(current_seq, longest)
        return longest
