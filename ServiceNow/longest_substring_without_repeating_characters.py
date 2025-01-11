# Leetcode: https://leetcode.com/problems/longest-substring-without-repeating-characters


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        hashmap = dict()
        length = len(s)
        front = 0
        back = 0
        maxi = -float("inf")
        while front < length:

            char = s[front]
            if hashmap.get(char) is None:
                hashmap[char] = front

            else:
                maxi = max(maxi, len(hashmap.keys()))
                update_ptr = hashmap[char] + 1
                for idx in range(back, update_ptr):
                    del hashmap[s[idx]]
                back = update_ptr
                hashmap[char] = front
            front += 1

        return max(maxi, len(hashmap.keys()))
    