package DSAlgo;

import java.util.*;

/**
 * https://leetcode.com/problems/count-square-submatrices-with-all-ones/
 *
 * @author parveenchahal
 */

public class CountSquareSubmatricesWithAllOnes {

    public int countSquares(int[][] matrix) {
        int count = 0;
        for (int i = 0; i < matrix.length; ++i) {
            for (int j = 0; j < matrix[0].length; ++j) {
                if (matrix[i][j] > 0 && i > 0 && j > 0) {
                    matrix[i][j] = Math.min(matrix[i - 1][j - 1], Math.min(matrix[i - 1][j], matrix[i][j - 1])) + 1;
                }
                count += matrix[i][j];
            }
        }
        return count;
    }
}

class CountSquareSubmatricesWithAllOnes1 {
    private boolean OnesRowsColumns(int[][] matrix, int i, int j, int s) {
        //for column
        for (int k = i; k < s + i; k++) {
            if(matrix[k][j + s - 1] != 1) {
                return false;
            }
        }
        
        //for row
        for (int k = j; k < s + j; k++) {
            if(matrix[i + s - 1][k] != 1) {
                return false;
            }
        }
        
        return true;
    }
    
    public int countSquares(int[][] matrix) {
        int N = matrix.length;
        int M = matrix[0].length;
        int S = Math.min(N, M);
        int count = 0;
        boolean[][][] dp = new boolean[N][M][S];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (matrix[i][j] == 1) {
                    dp[i][j][0] = true;
                    count++;
                }
            }
        }
        
        for (int s = 2; s <= S; s++) {
            for (int i = 0; i < N - s + 1; i++) {
                for (int j = 0; j < M - s + 1; j++) {
                    if (dp[i][j][s - 2] && OnesRowsColumns(matrix, i, j, s)) {
                        dp[i][j][s - 1] = true;
                        count++;
                    }
                }
            }
        }
        return count;
    }
}

class CountSquareSubmatricesWithAllOnes2 {

    public int countSquares(int[][] matrix) {
        int N = matrix.length;
        int M = matrix[0].length;
        int S = Math.min(N, M);
        int count = 0;
        boolean[][][] squareDP = new boolean[N][M][S];
        boolean[][][] rowDP = new boolean[N][M][S];
        boolean[][][] columnDP = new boolean[N][M][S];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (matrix[i][j] == 1) {
                    squareDP[i][j][0] = true;
                    rowDP[i][j][0] = true;
                    columnDP[i][j][0] = true;
                    count++;
                }
            }
        }
        
        for (int s = 2; s <= S; s++) {
            for (int i = 0; i < N - s + 1; i++) {
                for (int j = 0; j < M - s + 1; j++) {
                    rowDP[i + s - 1][j][s - 1] = matrix[i + s - 1][j + s - 1] == 1 && rowDP[i + s - 1][j][s - 2];
                    columnDP[i][j + s -1][s - 1] = matrix[i + s - 1][j + s - 1] == 1 && columnDP[i][j + s - 1][s - 2];
                    if (squareDP[i][j][s - 2] && rowDP[i + s - 1][j][s - 1] && columnDP[i][j + s -1][s - 1]) {
                        squareDP[i][j][s - 1] = true;
                        count++;
                    }
                }
            }
        }
        return count;
    }
}