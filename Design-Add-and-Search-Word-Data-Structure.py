"""
  Use a trie to hold words in an efficient way, adddword works by simply adding each letter to the try ione letter at a time.
  the search function first checks if the current node is a dot and if it is we run dfs on each of the children of the current node to see if they match the word we are looking for.
  If any of them do we return true straight away and if none of the children match the specific word we return false.
  O(n) time O(n + m) space.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.end
        return dfs(0, self.root)
