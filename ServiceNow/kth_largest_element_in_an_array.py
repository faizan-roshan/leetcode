# Leetcode: https://leetcode.com/problems/kth-largest-element-in-an-array

from typing import List
from heapq import heapify, heappop, heappush


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = []
        heapify(heap)
        for num in nums:

            heappush(heap, -1 * num)

        res = 0
        for i in range(0, k):

            res = heappop(heap)

        return res * -1
