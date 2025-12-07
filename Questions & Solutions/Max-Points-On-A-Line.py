class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        """
        I calculated the maximum points on a line by treating each point as a
        reference and counting how many other points share the same slope with
        it. I use atan2 to compute the angle between the reference point and
        each other point, which effectively represents the slope while handling
        vertical lines. For each reference point, I store slope counts in a
        hash map and find the maximum count. I add 1 to include the reference
        point itself. The overall maximum across all reference points gives the
        answer. This avoids slope division issues and handles all edge cases.
        O(n²) time O(n) space
        """
        n = len(points)
        if n == 1:
            return 1
        result = 2
        for i in range(n):
            cnt = collections.defaultdict(int)
            for j in range(n):
                if j != i:
                    cnt[
                        math.atan2(
                            points[j][1] - points[i][1],
                            points[j][0] - points[i][0],
                        )
                    ] += 1
            result = max(result, max(cnt.values()) + 1)
        return results