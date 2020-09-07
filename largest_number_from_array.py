#
# https://www.interviewbit.com/problems/largest-number/
#

from functools import cmp_to_key

def cmp(x, y):
    t = x
    x += y
    y += t
    if y.__eq__(x): return 0
    if y.__lt__(x): return -1
    if y.__gt__(x): return 1

def largest_number(A):
    A = [str(x) for x in A]
    A = sorted(A, key=cmp_to_key(cmp))
    return int(''.join(A))

r = largest_number([ 931, 94, 209, 448, 716, 903, 124, 372, 462, 196, 715, 802, 103, 740, 389, 872, 615, 638, 771, 829, 899, 999, 29, 163, 342, 902, 922, 312, 326, 817, 288, 75, 37, 286, 708, 589, 975, 747, 743, 699, 743, 954, 523, 989, 114, 402, 236, 855, 323, 79, 949, 176, 663, 587, 322 ])

assert r == 9999899759549499493192290390289987285582981780279771757477437437407167157086996636386155895875234624484023893737234232632332231229288286236209196176163124114103
