#
# https://www.interviewbit.com/problems/min-sum-path-in-triangle/
#

def minimum_total(A):
    for i in reversed(range(len(A) - 1)):
        for j in range(len(A[i])):
            A[i][j] += min(A[i + 1][j], A[i + 1][j + 1])
    return A[0][0]
        
if __name__ == '__main__':
    x = minimum_total([
        [2],
        [3,4],
    [6,5,7],
    [4,1,8,3]
    ])
    
    print(x)