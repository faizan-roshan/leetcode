# Leetcode: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        low = 0
        high = len(nums) - 1

        target_idx = -1
        while low <= high:

            mid = (high + low) // 2

            if nums[mid] == target:
                target_idx = mid
                break
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1

        if target_idx == -1:
            return [-1, -1]
        else:

            first, last = target_idx, target_idx
            while first - 1 >= 0:

                if first - 1 >= 0 and nums[first - 1] == target:
                    first = first - 1
                else:
                    break

            while last + 1 < len(nums):

                if last + 1 < len(nums) and nums[last + 1] == target:
                    last = last + 1
                else:
                    break

            return [first, last]
