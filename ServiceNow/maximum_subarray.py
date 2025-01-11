# Leetcode: https://leetcode.com/problems/maximum-subarray/

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        until_here = 0
        maximum = -1 * float('inf')
        for idx, num in enumerate(nums):

            until_here = max(until_here + num, num)
            maximum = max(maximum, until_here)
        return maximum
