import java.util.Collection;
import java.util.Collections;
import java.util.Comparator;

public class ArrayManipulation {
    static long arrayManipulation(int n, int[][] queries) {
        int[] arr = new int[n + 1];
        for(int[] query : queries) {
            int s = query[0] - 1;
            int e = query[1];
            int x = query[2];
            arr[s] += x;
            arr[e] -= x;
        }
        long curr = 0, max = 0;
        for(int x : arr) {
            curr += x;
            max = Math.max(max, curr);
        }
        return max;
    }

    public static void main(String[] args) {
        int n = 5;
        int[][] queries = {
            {1, 2, 100},
            {2, 5, 100},
            {3, 4, 100}
        };
        long r = arrayManipulation(n, queries);
        CodeTemplates.println(r);
    }
}
