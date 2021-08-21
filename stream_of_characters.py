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
            for c in w:
                if c not in t.children:
                    t.children[c] = Node(False)
                t = t.children[c]
            t.is_word = True
        #print(self.trie)
        self.list = []

    def query(self, letter: str) -> bool:
        found = False
        nl = []
        self.list.append(self.trie)
        for l in self.list:
            try:
                x = l.children[letter]
                nl.append(x)
                if x.is_word:
                    found = True
            except KeyError:
                pass
        self.list = nl
        return found
