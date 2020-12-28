// https://www.interviewbit.com/problems/spiral-order-matrix-ii/

import java.util.*;

public class SpiralOrderMatrix2 {
    static public ArrayList<ArrayList<Integer>> generateMatrix(int n) {
        int[][] mat = new int[n][n];
        int min_row = 0;
        int max_row = n - 1;
        int min_col = 0;
        int max_col = n - 1;

        int count = 1;

        do {
            for(int i = min_col; i <= max_col; i++) {
                mat[min_row][i] = count++;
            }
            min_row++;

            for(int i = min_row; i <= max_row; i++) {
                mat[i][max_col] = count++;
            }
            max_col--;

            for(int i = max_col; i >= min_col; i--) {
                mat[max_row][i] = count++;
            }
            max_row--;

            for(int i = max_row; i >= min_row; i--) {
                mat[i][min_col] = count++;
            }
            min_col++;

        } while(min_col <= max_row && min_col <= max_col);

        ArrayList<ArrayList<Integer>> result = new ArrayList<>();
        for(int[] row : mat) {
            ArrayList<Integer> temp = new ArrayList<>();
            for(int x : row) {
                temp.add(x);
            }
            result.add(temp);
        }
        return result;
    }

    public static void main(String[] args) {
        generateMatrix(2);
    }
}
