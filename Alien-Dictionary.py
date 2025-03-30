"""
  Loop through each word 2 at a time and compare against the conditions given, if any conditions are not met we return the empty string immediately.
  Otherwise we find the first differing character for each word and add it to our adjacency list as mapping one before another lexicographically.
  Afterward we run topological sort using dfs to get our return order of letters, if a cycle is detected we return the empty string also as it is not validlly sorted.
  O(N + V + E) time and O(V + E) space.
"""

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visited = {}
        res = []

        def dfs(char):
            if char in visited:
                return visited[char]

            visited[char] = True

            for neighChar in adj[char]:
                if dfs(neighChar):
                    return True

            visited[char] = False
            res.append(char)

        for char in adj:
            if dfs(char):
                return ""

        return "".join(res[::-1])
