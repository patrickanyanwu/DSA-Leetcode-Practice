"""
I used BFS to find the shortest
transformation sequence from beginWord to
endWord. For each word, I tried replacing
each character with all 26 letters, checking
if the new word exists in the word list and
hasn't been visited. BFS ensures I find the
shortest path, returning the step count when
reaching endWord.
O(n * m^2 * 26) time O(n) space
"""

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset = set(wordList)
        if endWord not in wordset:
            return 0
        
        charset = string.ascii_lowercase
        
        q = deque([(beginWord, 1)])
        seen = set([beginWord])
        
        while q:
            word, step = q.popleft()
            
            if word == endWord:
                return step
            
            for i in range(len(word)):
                for ch in charset:
                    if ch == word[i]:
                        continue
                    newword = word[:i] + ch + word[i+1:]
                    if newword in wordset and newword not in seen:
                        seen.add(newword)
                        q.append((newword, step + 1))
        
        return 0