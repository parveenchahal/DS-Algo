#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def merge(arr, l, mid, r):
    i = l
    j = mid + 1
    temp_list = []
    inv = 0
    while i <= mid and j <= r:
        if arr[i] <= arr[j]:
            temp_list.append(arr[i])
            i += 1
        else:
            inv += mid - i + 1
            temp_list.append(arr[j])
            j += 1
    if i <= mid:
        for k in range(i, mid + 1):
            temp_list.append(arr[k])
    if j <= r:
        for k in range(j, r + 1):
            temp_list.append(arr[k])
    for k in range(l, r + 1):
        arr[k] = temp_list.pop(0)
    return inv

def merge_sort(arr, l, r):
    inv = 0
    if l < r:
        mid = (l + r) // 2
        inv = merge_sort(arr, l, mid)
        inv += merge_sort(arr, mid + 1, r)
        inv += merge(arr, l, mid, r)
    return inv

def minimumBribes(q):
    n = len(q)
    for i in range(n):
        x = q[i] - i - 1
        if x > 2:
            return "Too chaotic"
    inv = merge_sort(q, 0, n - 1)
    return inv

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        r = minimumBribes(q)
        print(r)
