"""
  Keep track of a total cost and total gas as we loop through,
  we also keep track of our current tank
  if the current tank becomes negative we know we cant reach everywhere from where we are
  so we change our start position and reset our tank.
  we then return our start index if we have enough gas to go around the entire array
  if not we return -1.
  O(n) time O(1) space.
  
"""

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas, total_cost = 0, 0
        tank = 0
        start = 0
        
        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            tank += gas[i] - cost[i]

            if tank < 0:
                start = i + 1
                tank = 0
        
        return start if total_gas >= total_cost else -1
