"""
I implemented a hash map using separate chaining to handle collisions. I
create 1000 buckets, each containing a list of key-value pairs. The hash
function uses modulo to map keys to bucket indices. For put(), I hash the key
and check if it already exists in that bucket; if so, I update its value,
otherwise I append the new pair. For get(), I hash the key and search its
bucket for a matching key, returning the value or -1 if not found. For
remove(), I filter out the key-value pair from the bucket using a list
comprehension. This approach handles collisions efficiently through chaining.
O(n/k) average time per operation where k is bucket count, O(n) space
"""

class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        h = self._hash(key)
        for i, (k, v) in enumerate(self.buckets[h]):
            if k == key:
                self.buckets[h][i] = (key, value)
                return
        self.buckets[h].append((key, value))

    def get(self, key: int) -> int:
        h = self._hash(key)
        for k, v in self.buckets[h]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        h = self._hash(key)
        self.buckets[h] = [(k, v) for k, v in self.buckets[h] if k != key]