# https://leetcode.com/problems/sentence-similarity-iii/

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if sentence1 == sentence2:
            return True
        
        x = sentence1.split(' ')
        y = sentence2.split(' ')
        n1 = len(x)
        n2 = len(y)
        if n1 == 1 or n2 == 1:
            return x[0] == y[0] or x[-1] == y[-1]
        i1 = 0
        i2 = 0
        while i1 < n1 and i2 < n2 and x[i1] == y[i2]:
            i1 += 1
            i2 += 1
        i1 -= 1
        i2 -= 1
        
        j1 = n1 - 1
        j2 = n2 - 1
        while j1 >= 0 and j2 >= 0 and x[j1] == y[j2]:
            j1 -= 1
            j2 -= 1
        j1 += 1
        j2 += 1
        
        return i1 + 1 == j1 or i2 + 1 == j2
        