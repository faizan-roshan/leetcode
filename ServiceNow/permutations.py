# Leetcode: https://leetcode.com/problems/permutations/

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self._backtrack(nums, 0, result)
        return result

    def _backtrack(self, nums: List[int], idx: int, result: List[List[int]]):
        # Base case: if idx reaches the end, store the permutation
        if idx == len(nums):
            result.append(nums[:])  # Create a shallow copy of nums
            return

        # Recursive case: generate permutations by swapping
        for i in range(idx, len(nums)):
            nums[i], nums[idx] = nums[idx], nums[i]  # Swap
            self._backtrack(nums, idx + 1, result)  # Recurse
            nums[i], nums[idx] = nums[idx], nums[i]  # Backtrack
