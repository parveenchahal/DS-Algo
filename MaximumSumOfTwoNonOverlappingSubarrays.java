package DSAlgo;

/**
 * Leetcode-
 * https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/
 *
 * @author parveenchahal
 */
public class MaximumSumOfTwoNonOverlappingSubarrays {

    public int maxSumTwoNoOverlap(int[] A, int L, int M) {
        int N = A.length;

        int result = 0;

        int[] sumSoFar = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            sumSoFar[i] = sumSoFar[i - 1] + A[i - 1];
        }

        int[] lSumMaxSoFar = new int[N + 1];
        int[] mSumMaxSoFar = new int[N + 1];

        for (int i = L; i <= N; i++) {
            lSumMaxSoFar[i] = Math.max(lSumMaxSoFar[i - 1], sumSoFar[i] - sumSoFar[i - L]);
        }

        for (int i = M; i <= N; i++) {
            mSumMaxSoFar[i] = Math.max(mSumMaxSoFar[i - 1], sumSoFar[i] - sumSoFar[i - M]);
        }

        for (int i = L + M; i <= N; i++) {
            result = Math.max(result, sumSoFar[i] - sumSoFar[i - L] + mSumMaxSoFar[i - L]);
            result = Math.max(result, sumSoFar[i] - sumSoFar[i - M] + lSumMaxSoFar[i - M]);
        }

        return result;
    }
}
