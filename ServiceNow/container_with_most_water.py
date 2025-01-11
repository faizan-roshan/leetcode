# Leetcode: https://leetcode.com/problems/container-with-most-water/

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        max_area = 0
        back, front = 0, len(height) - 1

        while back < front:

            area = min(height[back], height[front]) * (front - back)
            max_area = max(area, max_area)

            if height[back] < height[front]:
                back += 1
            else:
                front -= 1

        return max_area
