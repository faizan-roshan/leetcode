# Leetcode: https://leetcode.com/problems/group-anagrams/

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = {}
        for string in strs:

            curr_sorted_string = "".join(sorted(string))
            if hashmap.get(curr_sorted_string) is None:
                hashmap[curr_sorted_string] = [string]
            else:
                hashmap[curr_sorted_string].append(string)

        return list(hashmap.values())
