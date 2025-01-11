# Leetcode: https://leetcode.com/problems/asteroid-collision/

from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)

            elif len(stack) != 0 and asteroid < 0 and stack[-1] > 0:

                last_pop = None
                while len(stack) != 0 and stack[-1] > 0:
                    if stack[-1] < abs(asteroid):
                        last_pop = stack.pop()
                        continue
                    elif stack[-1] == abs(asteroid):
                        last_pop = stack.pop()
                        break
                    else:
                        break

                if len(stack) == 0 and last_pop != abs(asteroid):
                    stack.append(asteroid)
                elif len(stack) > 0 and stack[-1] < 0 and last_pop != abs(asteroid):
                    stack.append(asteroid)

            elif len(stack) >= 0 or stack[-1] < 0:
                stack.append(asteroid)
        return stack
