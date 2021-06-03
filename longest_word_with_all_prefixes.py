# https://leetcode.com/problems/longest-word-with-all-prefixes/

from typing import List

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        s = set()
        for x in words:
            if len(x) == 1:
                s.add(x)
                continue
            if x[:-1] in s:
                s.add(x)
        result_list = ""
        max_len = 0
        for x in s:
            cur_len = len(x)
            if cur_len > max_len:
                max_len = cur_len
                result_list = x
            elif cur_len == max_len and x < result_list:
                result_list = x
        return result_list
                