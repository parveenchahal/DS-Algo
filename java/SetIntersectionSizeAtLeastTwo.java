import java.util.*;

/**
 * Leetcode- https://leetcode.com/problems/set-intersection-size-at-least-two/
 * 
 * @author parveenchahal
 */
public class SetIntersectionSizeAtLeastTwo {
    public int intersectionSizeTwo(int[][] intervals) {
        //Sort the interval with end point
        Arrays.sort(intervals, (a, b) -> (a[1] - b[1]));
        int N = intervals.length;
        int[] count = new int[N];
        int result = 0;
        for (int i = 0; i < N; i++) {
            for (int r = intervals[i][1]; r >= intervals[i][0] && count[i] < 2; r--) {
                result++;
                count[i]++;
                for (int j = i + 1; j < N; j++) {
                    if (r >= intervals[j][0] && r <= intervals[j][1]) {
                        count[j]++;
                    }
                }
            }
        }
        return result;
    }
}
