class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        """
        I checked if the array can form an arithmetic progression by first
        sorting it. In an arithmetic progression, the difference between
        consecutive elements must be constant. I calculate the difference
        between the first two elements and store it. Then I iterate through the
        remaining elements, checking if each consecutive difference matches the
        first one. If any difference is different, I return False. If all
        differences match, the array forms an arithmetic progression and I
        return True. Sorting ensures elements are in order.
        O(n log n) time O(1) space
        """
        arr.sort()
        prev_diff = arr[1] - arr[0]
        for i in range(2, len(arr)):
            diff = arr[i] - arr[i - 1]
            if diff != prev_diff:
                return False
        return True