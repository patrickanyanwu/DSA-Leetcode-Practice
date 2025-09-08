"""Implement a trie data structure that allows for efficient prefix searching in words."""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
            if curr.end == True and c == word[-1]:
                return True
        return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i, c in enumerate(list(prefix)):
            if c in curr.children:
                if i == len(prefix) - 1:
                    return True
                curr = curr.children[c]
            else:
                return False
