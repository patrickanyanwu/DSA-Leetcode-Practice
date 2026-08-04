"""
I implemented bucket sort for floats in the
range [0, 1) by creating n buckets and
distributing values based on their decimal
value. I sorted each bucket individually
and merged them to get the final result.
O(n) time O(n) space
"""

def bucket_sort(arr):
    n = len(arr)
    if n == 0:
        return arr

    buckets = [[] for _ in range(n)]

    for value in arr:
        index = int(value * n)
        if index == n:
            index -= 1
        buckets[index].append(value)

    for i in range(n):
        buckets[i].sort()

    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr