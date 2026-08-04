class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        """
        I simulated the robot's movement to determine if it's bounded in a
        circle. I use direction vectors for north, east, south, west and track
        position (x, y) and direction index d. For 'G', I move in the current
        direction; for 'L', I rotate left (d-1 mod 4); for 'R', I rotate right
        (d+1 mod 4). After one instruction cycle, the robot is bounded if it
        returns to origin OR faces a different direction (not north). If it
        faces a different direction, it will return to origin after at most 4
        cycles. This key insight avoids simulating multiple cycles.
        O(n) time O(1) space
        """
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x = y = 0
        d = 0  

        for ch in instructions:
            if ch == 'G':
                x += dirs[d][0]
                y += dirs[d][1]
            elif ch == 'L':
                d = (d - 1) % 4
            else:  # 'R'
                d = (d + 1) % 4

        return (x == 0 and y == 0) or d != 0