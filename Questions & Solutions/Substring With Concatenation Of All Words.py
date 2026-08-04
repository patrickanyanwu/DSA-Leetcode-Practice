"""
  The code identifies all starting indices in a string s where a substring is formed by the concatenation of all words from the list words, in any order and without any extra characters.
  It calculates the total length of the concatenated words and uses a sliding window approach, checking fixed-size windows across different offsets.
  For each window, it uses counters to track how often each word appears and compares it to the expected counts.
  When a match is found—meaning all words appear exactly as required—it adds the starting index to the result.
  This method ensures efficient checking across the string without redundant computation.
  O(n * m) time O(m) space, n is  len(s) and m is len(words)
"""


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_count = Counter(words)
        result = []

        for i in range(word_len):
            left = i
            right = i
            current_count = Counter()

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word in word_count:
                    current_count[word] += 1

                    while current_count[word] > word_count[word]:
                        current_count[s[left:left + word_len]] -= 1
                        left += word_len

                    if right - left == total_len:
                        result.append(left)
                else:
                    current_count.clear()
                    left = right

        return result
