# Leetcode: https://leetcode.com/problems/first-unique-character-in-a-string/

from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:

        s_freq = Counter(s)
        for idx, char in enumerate(s):
            if s_freq.get(char) == 1:
                return idx
        return -1
