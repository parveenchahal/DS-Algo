# https://leetcode.com/problems/valid-number/

class Solution:
    def isNumber(self, s: str) -> bool:
        # d is digit[0, 9]
        dfa = [
            {"d": 1, "+-": 2, ".": 3},
            {"d": 1, ".": 4, "e": 5},
            {"d": 1, ".": 3},
            {"d": 4},
            {"d": 4, "e": 5},
            {"+-": 6, "d": 7},
            {"d": 7},
            {"d": 7}
        ]
        
        current_state = 0
        try:
            for x in s:
                if x >= '0' and x <= '9':
                    current_state = dfa[current_state]['d']
                elif x in ["+", "-"]:
                    current_state = dfa[current_state]['+-']
                elif x in ["e", "E"]:
                    current_state = dfa[current_state]['e']
                elif x == ".":
                    current_state = dfa[current_state]['.']
                else:
                    return False
        except KeyError:
            return False
        return current_state in [1, 4, 7]
