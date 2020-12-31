// https://leetcode.com/problems/average-waiting-time/

public class AverageWaitingTime {
    public double averageWaitingTime(int[][] customers) {
        int curr = 0;
        double avgWait = 0;
        for(int[] customer : customers) {
            curr = Math.max(curr, customer[0]);
            curr += customer[1];
            avgWait += curr - customer[0];
        }
        return avgWait / customers.length;
    }

    public static void main(String[] args) {
        int[][] customers = {
            {5, 2},
            {5, 4},
            {10, 3},
            {20, 1}
        };
        double r = new AverageWaitingTime().averageWaitingTime(customers);
        CodeTemplates.println(String.format("%.5f", r));
    }
}
