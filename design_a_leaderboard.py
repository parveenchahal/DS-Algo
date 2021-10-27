# https://leetcode.com/problems/design-a-leaderboard/


from sortedcontainers import SortedDict

class Leaderboard:

    def __init__(self):
        self._scores = {}
        self._sorted_map = SortedDict()

    def addScore(self, playerId: int, score: int) -> None:
        prev = 0
        if playerId in self._scores:
            prev = self._scores[playerId]
            if -prev in self._sorted_map:
                self._sorted_map[-prev] -= 1
                if self._sorted_map[-prev] == 0:
                    del self._sorted_map[-prev]
        new_score = prev + score
        self._scores[playerId] = new_score
        if -new_score in self._sorted_map:
            self._sorted_map[-new_score] += 1
        else:
            self._sorted_map[-new_score] = 1
    
    def top(self, K: int) -> int:
        res = 0
        for k,v in self._sorted_map.items():
            k = -k
            if K - v >= 0:
                res += k * v
                K -= v
            else:
                res += k * K
                break
        return res

    def reset(self, playerId: int) -> None:
        scr = self._scores[playerId]
        del self._scores[playerId]
        self._sorted_map[-scr] -= 1
        if self._sorted_map[-scr] == 0:
            del self._sorted_map[-scr]
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
