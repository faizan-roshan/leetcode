# Leetcode: https://leetcode.com/problems/valid-palindrome/


class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        p1, p2 = 0, len(s) - 1

        while p1 <= p2:

            if s[p1].isalnum() is False:
                p1 += 1
                continue
            if s[p2].isalnum() is False:
                p2 -= 1
                continue

            if s[p1] == s[p2]:
                p1 += 1
                p2 -= 1
                continue
            else:
                return False

        return True
