"""
I tracked the robot's position by simulating each move on a 2D coordinate
system. I start at origin [0, 0] and process each move character: 'U'
decreases row (moves up), 'D' increases row (moves down), 'L' decreases
column (moves left), and 'R' increases column (moves right). After processing
all moves, I check if the position returned to [0, 0]. If both coordinates
are zero, the robot returned to origin. This approach simulates the path
directly without needing any complex data structures.
O(n) time O(1) space
"""

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        pos = [0, 0]
        for mv in moves:
            if mv == "U":
                pos[0] -= 1
            elif mv == "D":
                pos[0] += 1
            elif mv == "L":
                pos[1] -= 1
            else:
                pos[1] += 1
        return pos[0] == 0 and pos[1] == 0