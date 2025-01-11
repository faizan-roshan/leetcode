# Leetcode: https://leetcode.com/problems/time-needed-to-rearrange-a-binary-string

class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        
        if "0" not in s:
            return 0

        count = 0
        while "01" in s:

            s = s.replace("01", "10")
            count += 1
        
        return count
    