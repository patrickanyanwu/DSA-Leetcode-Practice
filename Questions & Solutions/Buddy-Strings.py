"""
I checked if two strings can become equal by swapping exactly two characters
in one string. First, I verify lengths match. If strings are already equal, I
check if any character appears more than once (allowing a swap of duplicates).
If strings differ, I collect all differing positions in a list. There must be
exactly 2 differences, and the characters at those positions must be swapped
versions of each other (s[i] == goal[j] and s[j] == goal[i]). I verify this
by checking if diff[0] == diff[1][::-1], where [::-1] reverses the tuple. This
efficiently handles all cases in a single pass.
O(n) time O(n) space
"""

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal:
            seen = set()
            for c in s:
                if c in seen:
                    return True
                seen.add(c)
            return False

        diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append((s[i], goal[i]))
                if len(diff) > 2:
                    return False

        return len(diff) == 2 and diff[0] == diff[1][::-1]
