# https://leetcode.com/problems/string-to-integer-atoi/

MIN = -0x80000000
MAX = 0x7fffffff
class Solution:
    def _atoi(self, s):
        if len(s) <= 0:
            return 0
        neg = False
        if s[0] == '-':
            neg = True
            s = s[1:]
        n = len(s)
        res = 0
        for i in range(n):
            res *= 10
            res += ord(s[i]) - ord('0')
            if res > -MIN:
                break
            i -= 1
        res = res if not neg else -res
        if res < MIN:
            return MIN
        if res > MAX:
            return MAX
        return res
            
    def myAtoi(self, s: str) -> int:
        n = len(s)
        if n <= 0:
            return 0
        
        # Deterministic Finite Automata (DFA) 
        dfa = {
            0: {' ': 0, 's': 1, 'd': 2},
            1: {'d': 2},
            2: {'d': 2}
        }
        current_state = 0
        final_str = ''
        for i in range(n):
            try:
                if s[i] == ' ':
                    current_state = dfa[current_state][' ']
                elif s[i] == '+':
                    current_state = dfa[current_state]['s']
                elif s[i] == '-':
                    current_state = dfa[current_state]['s']
                    final_str += '-'
                elif s[i] >= '0' and s[i] <= '9':
                    current_state = dfa[current_state]['d']
                    final_str += s[i]
                else:
                    break
            except KeyError:
                break
        return self._atoi(final_str)
                
