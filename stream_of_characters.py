# https://leetcode.com/problems/stream-of-characters/

class Node:
    def __init__(self, is_word):
        self.children = {}
        self.is_word = is_word
    def __repr__(self):
        return f'<{str(self.children)}, {self.is_word}>'

class StreamChecker:
    def __init__(self, words: List[str]):
        self.trie = Node(False)
        for w in words:
            t = self.trie
            for c in w[::-1]:
                if c not in t.children:
                    t.children[c] = Node(False)
                t = t.children[c]
            t.is_word = True
        self.stream = deque()

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        t = self.trie
        for c in self.stream:
            try:
                t = t.children[c]
                if t.is_word:
                    return True
            except KeyError:
                return False
        return False
