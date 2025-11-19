"""
I implemented bucket sort by dividing the
range into buckets, distributing integers
into appropriate buckets based on their
value, sorting each bucket individually,
and merging them back together.
O(n + k) time O(n + k) space
"""

def bucket_sort_int(arr, bucket_size=5):
    if len(arr) == 0:
        return arr

    # 1. Determine minimum and maximum values
    min_value = min(arr)
    max_value = max(arr)

    # 2. Calculate number of buckets
    bucket_count = (max_value - min_value) // bucket_size + 1
    buckets = [[] for _ in range(bucket_count)]

    # 3. Distribute integers into buckets
    for num in arr:
        index = (num - min_value) // bucket_size
        buckets[index].append(num)

    # 4. Sort each bucket and merge
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))

    return sorted_arr