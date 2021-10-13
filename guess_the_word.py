# https://leetcode.com/problems/guess-the-word/


# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    
    def _match(self, w1, w2):
        count = 0
        for i in range(6):
            if w1[i] == w2[i]:
                count += 1
        return count
    
    def _filter(self, words, target, matches):
        res = []
        for w in words:
            if self._match(target, w) == matches:
                res.append(w)
        return res
    
    def _zero_matches(self, words, n, w):
        zm = 0
        for i in range(n):
            if self._match(w, words[i]) == 0:
                zm += 1
        return zm
    
    def _get_word_for_guess(self, words):
        n = len(words)
        res = words[n // 2]
        res_zm = self._zero_matches(words, n, words[n // 2])
        for i in range(n):
            zm = self._zero_matches(words, n, words[i])
            if zm < res_zm:
                res = words[i]
                res_zm = zm
        return res
    
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        for _ in range(10):
            if len(wordlist) == 0:
                return
            w = self._get_word_for_guess(wordlist)
            matches = master.guess(w)
            #print(f'{w} : {matches}')
            if matches == 6:
                return
            wordlist = self._filter(wordlist, w, matches)
