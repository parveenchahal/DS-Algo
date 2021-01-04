# https://leetcode.com/problems/count-good-meals/

from typing import List

def count_pairs(deliciousness: List[int]) -> int:
    pow_of_two = []
    cur = 1
    pow_of_two.append(cur)
    # Max 2^20 + 2^20 ~= 2 ^ 21
    for _ in range(1, 22):
        cur *= 2
        pow_of_two.append(cur)
    deliciousness_count = {}
    # Either count all freq initially and subtract one by one
    # Or Add in dict one by one and increase freq.
    result = 0
    for x in deliciousness:
        for p in pow_of_two:
            if p >= x:
                y = p - x
                if y in deliciousness_count:
                    c = deliciousness_count[y]
                    result += c
                    result %= 1000000007
        try:
            deliciousness_count[x] += 1
        except KeyError:
            deliciousness_count[x] = 1
    return result
    

r = count_pairs([1,1,1,3,3,3,7])
assert r == 15

r = count_pairs([1,3,5,7,9])
assert r == 4

r = count_pairs([149,107,1,63,0,1,6867,1325,5611,2581,39,89,46,18,12,20,22,234])
assert r == 12

