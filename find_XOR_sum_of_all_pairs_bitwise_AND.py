# https://leetcode.com/problems/find-xor-sum-of-all-pairs-bitwise-and/

from functools import reduce
from operator import xor

def get_xor_sum(arr1, arr2):
    xor2 = reduce(xor, arr2)
    l = [x & xor2 for x in arr1]
    return reduce(xor, l)

r = get_xor_sum([1, 2, 3], [6, 5])
assert r == 0