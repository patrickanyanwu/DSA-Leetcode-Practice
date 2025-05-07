"""
  Initialize a queue to hold all events,
  when a ping happens we discard of all events that arent in our range and we return the final length of the queue.
  O(n) time O(n) space.
"""

class RecentCounter:

    def __init__(self):
        self.events = deque()

    def ping(self, t: int) -> int:
        self.events.append(t)
        l = t - 3000
        while self.events[0] < l:
            self.events.popleft()
        return len(self.events)
