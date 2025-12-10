"""
I implemented stable counting sort by first
counting occurrences of each value, then
converting counts to positions, and finally
placing elements in their correct positions
by traversing the array in reverse.
O(n + k) time O(n + k) space
"""

def stable_counting_sort(arr):
    if len(arr) == 0:
        return arr

    max_val = max(arr)

    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    output = [0] * len(arr)

    for num in reversed(arr):
        count[num] -= 1
        output[count[num]] = num

    return output