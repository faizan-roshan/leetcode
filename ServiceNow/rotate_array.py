# Leetcode: https://leetcode.com/problems/rotate-array/

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums)  # Handle cases where k > len(nums)
        nums[:] = nums[-k:] + nums[:-k]
