"""
  Sort the products lexicographically so we can find (using binary search) the index of the first word that contains the current prefix,
  now for each word from that index onward (max of 3) we check if it starts with the prefix and if it does we add it to a sugesstions array,
  after we append that array to our result array.
  O(n log n) time O(n) space
"""

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []
        prefix = ""
        for ch in searchWord:
            prefix += ch
            i = bisect.bisect_left(products, prefix)
            suggestions = []
            for w in products[i : min(i+3, len(products))]:
                if w.startswith(prefix):
                    suggestions.append(w)
                else:
                    break
            res.append(suggestions)
        return res
