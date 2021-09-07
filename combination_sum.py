# https://leetcode.com/problems/combination-sum/

# Method 1 (Backtracking)
class Solution:
    def _combination(self, i, buf, target, candidates, n, res):
        if target < 0:
            return
        if target == 0:
            res.append(list(buf))
        for j in  range(i, n):
            buf.append(candidates[j])
            self._combination(j, buf, target - candidates[j], candidates, n, res)
            buf.pop()
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        self._combination(0, [], target, candidates, n, res)
        return res


# Method 2 (DP)
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
         
