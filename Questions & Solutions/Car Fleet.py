"""
  Sort cars by position (closest to target first).
  Calculate time to reach target for each car: (target - position) / speed.
  Use a stack to track separate fleets. Process cars from front to back.
  If a car behind takes less or equal time than the car ahead, they form a fleet (pop from stack).
  Otherwise, it's a new fleet (keep in stack).
  The stack size at the end represents the number of fleets.
  O(n log n) time, O(n) space.
"""

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)