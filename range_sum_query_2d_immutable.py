# https://leetcode.com/problems/range-sum-query-2d-immutable/


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        R = len(matrix) + 1
        C = len(matrix[0]) + 1
        self._mat = [[0] * (C) for _ in range(R)]
        for i in range(1, R):
            for j in range(1, C):
                self._mat[i][j] = matrix[i - 1][j - 1] + self._mat[i - 1][j] + self._mat[i][j - 1] - self._mat[i - 1][j - 1]
    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        mat = self._mat
        return mat[row2 + 1][col2 + 1] - mat[row1][col2 + 1] - mat[row2 + 1][col1] + mat[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
