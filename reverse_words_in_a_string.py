# https://leetcode.com/problems/reverse-words-in-a-string/

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s[::-1]
        s = s.split(' ')
        s = list(filter(lambda x: x != '', s))
        r = [x[::-1] for x in s]
        return ' '.join(r)
