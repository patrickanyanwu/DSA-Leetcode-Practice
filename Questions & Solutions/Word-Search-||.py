"""Use a trie in order to be able to efficiently search for words based on previous characters,
we then run recursive backtracking on the matrix and if the current letter we are on in the trie is the end of a word we add that word to our result and we change that trie nodes end of word value to false to avoid duplicate work.
we use a seen set to avoid going back to the same characters in one path.
O(4** n) time and O(s) space with s being the number of letters in each word in the words array.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_end_of_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        ROWS, COLS = len(board), len(board[0])
        res = set()
        seen = set()

        def dfs(row, col, node, path):
            if (row < 0 or row >= ROWS or col < 0 or col >= COLS or 
                (row, col) in seen or board[row][col] not in node.children):
                return

            seen.add((row, col))
            node = node.children[board[row][col]]
            path += board[row][col]

            if node.is_end_of_word:
                res.add(path)
                node.is_end_of_word = False

            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                dfs(row + dr, col + dc, node, path)

            seen.remove((row, col))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie.root, "")

        return list(res)
