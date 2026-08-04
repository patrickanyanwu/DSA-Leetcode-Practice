"""
  Initialize a min heap and we add the first (candidates) elements with a 0
  to mark that it was from the left and we do the same with the right but mark it with a 1,
  now we set pointers at the next potential elments for each side.
  Now we loop through k times and we pop from the heap and
  if we popped from the left we add another element from the left to the heap and vice versa for the right.
  Throughout the loop we keep track of our cost sum.
  O(N log n) time O(n) space
"""

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        pq = []
        for i in range(candidates):
            pq.append((costs[i], 0))
        for i in range(max(candidates, len(costs) - candidates), len(costs)):
            pq.append((costs[i], 1))

        heapify(pq)
        
        answer = 0
        next_head, next_tail = candidates, len(costs) - 1 - candidates 

        for _ in range(k): 
            cur_cost, cur_section_id = heappop(pq)
            answer += cur_cost
            if next_head <= next_tail: 
                if cur_section_id == 0:
                    heappush(pq, (costs[next_head], 0))
                    next_head += 1
                else:
                    heappush(pq, (costs[next_tail], 1))
                    next_tail -= 1
                    
        return answer
