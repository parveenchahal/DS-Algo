# https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        m = target + 1
        dp = [[] for _ in range(m)]
        for i in range(n):
            for j in range(1, m):
                if j < candidates[i]:
                    continue
                elif j == candidates[i]:
                    dp[j].append([candidates[i]])
                else:
                    if len(dp[j - candidates[i]]) > 0:
                        t = copy.deepcopy(dp[j - candidates[i]])
                        for x in t:
                            x.append(candidates[i])
                        dp[j].extend(t)
        return dp[m - 1]
         
