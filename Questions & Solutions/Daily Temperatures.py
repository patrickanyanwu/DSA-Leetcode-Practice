"""
  We use a monotonically decreasing stack,
  as we loop through from left to right we push each temperature to our stack aswell as its index
  then when we reach a temperature that is greater than the temperature at the top of our stack we pop from the stack
  and set that index in our result equal to the difference of the current index and that index we just popped. This is done in
  a while loop to take care of every lower temperature.
  O(n) time O(1) space
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                temperature, index = stack.pop()
                res[index] = i - index
            stack.append([temp, i])
        return res
