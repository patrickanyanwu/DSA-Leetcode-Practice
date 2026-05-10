"""
Use a max heap to always execute the most frequent task next, with a cooldown queue to track when tasks become available again.
Count task frequencies and push them as negative values into a max heap (Python only has min heap).
Each time step, pop the most frequent task, decrement its count, and if still remaining, push it into a cooldown queue with the earliest time it can run again (current time + n).
If the heap is empty but the queue is not, jump time forward to when the next task is available.
When a task's cooldown expires (its ready time equals current time), push it back onto the heap.
Continue until both the heap and queue are empty.
O(t * n) time where t is total tasks and n is cooldown interval, O(1) space since at most 26 unique task characters.
"""

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()  # pairs of [-cnt, idleTime]
        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time