# Leetcode: https://leetcode.com/problems/two-sum/description/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for idx, num in enumerate(nums):
            val = target - num
            if val in seen:
                return [idx, seen[val]]

            seen[num] = idx


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([2, 7, 11, 15], 9),  # Expected output: [1, 0]
        ([3, 2, 4], 6),  # Expected output: [2, 1]
        ([3, 3], 6),  # Expected output: [1, 0]
        ([1, 5, 3, 7], 8),  # Expected output: [3, 0]
    ]

    solution = Solution()

    for nums_arr, target in test_cases:
        result = solution.twoSum(nums_arr, target)
        print(f"nums= {nums_arr} | target = {target} → result = {result}")
