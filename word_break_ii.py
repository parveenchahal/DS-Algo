# https://leetcode.com/problems/word-break-ii/


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        d = set(wordDict)
        res = [[] for _ in range(n + 1)]
        res[0] = [[]]
        for i in range(1, n + 1):
            for j in range(0, i):
                if s[j:i] in d:
                    for x in res[j]:
                        x = copy.deepcopy(x)
                        x.append(s[j:i])
                        res[i].append(x)
        return [' '.join(x) for x in res[n]]
