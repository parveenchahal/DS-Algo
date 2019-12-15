package DSAlgo;

import java.util.*;

/**
 * Leetcode- https://leetcode.com/problems/queens-that-can-attack-the-king/
 *
 * @author parveenchahal
 */
public class QueensThatCanAttackTheKing {

    private void updateAttackMap(String direction, int[] queen, Map<String, List<Integer>> attackMap, int[] king) {
        List<Integer> existQueen = attackMap.get(direction);
        if (existQueen == null) {
            List<Integer> list = new LinkedList<>();
            for (int x : queen) {
                list.add(x);
            }
            attackMap.put(direction, list);
            return;
        }
        switch (direction) {
            case "U":
                if (queen[0] > existQueen.get(0)) {
                    existQueen.set(0, queen[0]);
                }
                break;
            case "LU":
            case "RU":
                if (queen[0] > existQueen.get(0)) {
                    existQueen.set(0, queen[0]);
                    existQueen.set(1, queen[1]);
                }
                break;
            case "D":
                if (queen[0] < existQueen.get(0)) {
                    existQueen.set(0, queen[0]);
                }
                break;
            case "LD":
            case "RD":
                if (queen[0] < existQueen.get(0)) {
                    existQueen.set(0, queen[0]);
                    existQueen.set(1, queen[1]);
                }
                break;
            case "L":
                if (queen[1] > existQueen.get(1)) {
                    existQueen.set(1, queen[1]);
                }
                break;
            case "R":
                if (queen[1] < existQueen.get(1)) {
                    existQueen.set(1, queen[1]);
                }
                break;

        }
    }

    private void queenAttack(int[] queen, int[] king, Map<String, List<Integer>> attackMap) {
        String direction = null;
        if (queen[0] == king[0] && queen[1] < king[1]) {
            direction = "L";
        } else if (queen[0] == king[0] && queen[1] > king[1]) {
            direction = "R";
        } else if (queen[1] == king[1] && queen[0] < king[0]) {
            direction = "U";
        } else if (queen[1] == king[1] && queen[0] > king[0]) {
            direction = "D";
        } else if (Math.abs(queen[0] - king[0]) == Math.abs(queen[1] - king[1])) {
            if (queen[1] < king[1]) {
                direction = "L";
            } else {
                direction = "R";
            }
            if (queen[0] < king[0]) {
                direction += "U";
            } else {
                direction += "D";
            }
        }
        if (direction != null) {
            updateAttackMap(direction, queen, attackMap, king);
        }
    }

    public List<List<Integer>> queensAttacktheKing(int[][] queens, int[] king) {
        List<List<Integer>> result = new LinkedList<>();
        Map<String, List<Integer>> attackMap = new HashMap<>();
        for (int[] queen : queens) {
            queenAttack(queen, king, attackMap);
        }
        return new LinkedList<>(attackMap.values());
    }
}
