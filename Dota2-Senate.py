"""
  Initialize a queue which holds the indexes of each party,
  We then run a while loop in which we pop from the left of the queue and whichever index is lower wins that round and the other party loses one "vote".
  We re-add to the winners queue for subsequent rounds.
  We then return which queue still has items in it (winner).
  O(n) time O(n) space
  
"""

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant_queue = deque()
        dire_queue = deque()

        for i, senator in enumerate(senate):
            if senator == "R":
                radiant_queue.append(i)
            else:
                dire_queue.append(i)

        while radiant_queue and dire_queue:
            radiant_senator = radiant_queue.popleft()
            dire_senator = dire_queue.popleft()

            if radiant_senator < dire_senator:
                radiant_queue.append(radiant_senator + len(senate))
            else:
                dire_queue.append(dire_senator + len(senate))
                
        return "Radiant" if radiant_queue else "Dire"
