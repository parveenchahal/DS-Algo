# https://leetcode.com/problems/prefix-and-suffix-search/


class Node:
    def __init__(self):
        self.word_index = 0
        self.children = defaultdict(Node)
        
    def __repr__(self):
        return f'({str(self.word_index)}, {str(self.children)})'
        

class WordFilter:

    def __init__(self, words: List[str]):
        self._words = words
        self._trie = Node()
        for i,word in enumerate(words):
            self._add(word, i)
        
    def _add(self, word, index):
        n = len(word)
        rev_word = ''.join(reversed(word))
        trie = self._trie
        for i in range(n):
            tmp = trie
            for c in word[i:]:
                tmp = tmp.children[(c, None)]
                tmp.word_index = index
            
            tmp = trie
            for c in rev_word[i:]:
                tmp = tmp.children[(None, c)]
                tmp.word_index = index

            trie = trie.children[(word[i], rev_word[i])]
            trie.word_index = index
        
    def f(self, prefix: str, suffix: str) -> int:
        pl = len(prefix)
        sl = len(suffix)
        suffix = ''.join(reversed(suffix))
        max_len = max(pl, sl)
        trie = self._trie
        for i in range(max_len):
            p = prefix[i] if i < pl else None
            s = suffix[i] if i < sl else None
            pre_suf = (p, s)
            if pre_suf not in trie.children:
                return -1
            trie = trie.children[pre_suf]
        return trie.word_index
