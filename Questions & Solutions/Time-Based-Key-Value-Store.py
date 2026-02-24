"""
  Use a hashmap where each key maps to a list of (value, timestamp) tuples.
  For set: append the (value, timestamp) to the key's list. Since timestamps are strictly increasing, the list stays sorted.
  For get: use binary search on the key's list to find the largest timestamp <= the requested timestamp.
  Keep track of the most recent valid value as res, moving left pointer up when timestamp is valid, right pointer down when too large.
  Return the stored res or empty string if key doesn't exist or no valid timestamp found.
  O(log n) time for get, O(1) time for set, O(n) space where n is total number of set operations.
"""

class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        
        values = self.map[key]

        l, r = 0, len(values) - 1
        res = ""
        while l <= r:
            mid = l + (r - l) // 2

            value, ts = values[mid]

            if ts <= timestamp:
                res = value
                l = mid + 1
            else:
                r = mid - 1

        return res
