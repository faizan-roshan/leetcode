# Leetcode: https://leetcode.com/problems/move-zeroes/

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if len(nums) < 2:
            return nums

        idx2 = 0
        length = len(nums)
        for idx1, num in enumerate(nums):

            if num == 0:

                if idx2 < idx1:
                    idx2 = idx1 + 1
                while idx2 < length and nums[idx2] == 0:

                    idx2 += 1

                if idx2 < length:
                    nums[idx1], nums[idx2] = nums[idx2], nums[idx1]
