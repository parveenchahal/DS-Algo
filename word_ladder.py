# https://leetcode.com/problems/word-ladder/

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        chars = [chr(ord('a') + i) for i in range(26)]
        q = deque()
        q.append((beginWord, 1))
        visited = set()
        visited.add(beginWord)
        while len(q) > 0:
            x, d = q.popleft()
            for i in range(len(x)):
                for c in chars:
                    t = x[:i] + c + x[i + 1:]
                    if t in words and t not in visited:
                        if t == endWord:
                            return d + 1
                        visited.add(t)
                        q.append((t, d + 1))
                        
        return 0
