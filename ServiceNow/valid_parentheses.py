# Leetcode: https://leetcode.com/problems/valid-parentheses/description/


class Solution:
    def isValid(self, s: str) -> bool:

        hmap = {"}": "{", "]": "[", ")": "("}
        stack = []
        for para in s:

            # para is closing parentheses
            if para in hmap.keys() and len(stack) > 0 and stack[-1] == hmap.get(para):
                stack.pop()
                continue

            stack.append(para)

        if stack:
            return False

        return True
