"""
I used a hash map to store numbers and their
frequencies. For add, I updated the count.
For find, I checked if the complement exists
in the map, handling duplicates by ensuring
the count is greater than 1 for same number.
O(1) add, O(n) find time O(n) space
"""

class TwoSum:

    def __init__(self):
        self.nums_map = {}

    def add(self, number: int) -> None:
        self.nums_map[number] = self.nums_map.get(number, 0) + 1

    def find(self, value: int) -> bool:
        for num in self.nums_map:
            diff = value - num
            if diff in self.nums_map:
                if diff != num or self.nums_map[num] > 1:
                    return True
        return False