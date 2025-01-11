# Leetcode: https://leetcode.com/problems/first-missing-positive/

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        nums = [num for num in nums if num > 0]

        for num in nums:

            idx = abs(num) - 1
            if idx < len(nums) and nums[idx] > 0:
                nums[idx] = nums[idx] * -1

        for i in range(0, len(nums)):

            if nums[i] > 0:
                return i + 1

        return len(nums) + 1
