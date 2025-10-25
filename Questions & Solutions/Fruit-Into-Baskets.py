"""
    Use a hashmap which holds each unique element in our window as key and its frequency count as value,
    As we open our window we update our hashmap and increment the count of fruits.
    While we have too many unique fruits we decrement the count of the fruit at the beginning of our window and 
    close the window. Whule we loop through we always keep a global max count fo fruits
    O(n) time O(n) space.
"""


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = total = l = 0
        unique = {}
        for r in range(len(fruits)):
            unique[fruits[r]] = unique.get(fruits[r], 0) + 1
            count += 1
            while len(unique) > 2:
                unique[fruits[l]] -= 1
                if unique[fruits[l]] <= 0:
                    del unique[fruits[l]]
                count -= 1
                l = l + 1
            total = max(total, count)
        return total                