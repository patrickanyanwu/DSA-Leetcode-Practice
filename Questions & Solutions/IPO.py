class Solution:
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        I used a greedy approach with a max heap to maximize capital. I first
        sort projects by capital requirement, then for each of k iterations, I
        add all affordable projects (capital requirement <= current w) to a max
        heap based on profit. I use negative values since Python's heapq is a
        min heap. I then select the most profitable project from the heap and
        add its profit to my capital. This ensures I always choose the highest
        profit among affordable options. If no projects are affordable, I break
        early. This greedy strategy maximizes capital gain.
        O(n log n) time O(n) space
        """
        projects = sorted(zip(capital, profits))
        maxheap = []
        i = 0
        n = len(projects)

        for _ in range(k):
            while i < n and projects[i][0] <= w:
                cap, prof = projects[i]
                heappush(maxheap, -prof)
                i += 1

            if not maxheap:
                break

            w += -heappop(maxheap)

        return w