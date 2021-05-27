# https://www.interviewbit.com/problems/next-similar-number/

def reverse(arr, i, j):
    while(i < j):
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        arr = [int(x) for x in A]
        n = len(arr)
        if n < 2:
            return -1
        prev = arr[n - 1]
        for i in range(n - 2, -1, -1):
            if arr[i] < prev:
                j = n - 1
                while(j > i):
                    if arr[j] > arr[i]:
                        break
                    j -= 1
                arr[i], arr[j] = arr[j], arr[i]
                reverse(arr, i + 1, n - 1)
                t_s = [str(x) for x in arr]
                r = "".join(t_s)
                return r if r != A else -1
            prev = arr[i]
        return -1