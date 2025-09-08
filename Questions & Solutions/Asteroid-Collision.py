"""
  We use a stack to keep track of asteroids,
  if we meet an asteroid moving left and the last asteroid in the stack is moving to the right we pop that asteroid from the stack,
  and append the absolutely bigger element to the stack.
  If they are equal in size we dont append anything to the stack.
  We do this in a while loop so that the asteroid destroys every asteroid it could collide with.
  Return stack.
  O(n) time O(n) space.
"""

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for a in asteroids:
            while a < 0 and stack and stack[-1] > 0:
                prev = stack.pop()
                if abs(a) > prev:
                    continue 
                elif abs(a) == prev:
                    break
                else:
                    stack.append(prev)
                    break
            else:
                stack.append(a)
                
        return stack
