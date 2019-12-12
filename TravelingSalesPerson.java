package DSAlgo;


import java.io.*;
import java.util.*;

/**
 * Input:
 * 4 4
 * 0 1 15 6
 * 2 0 7 3
 * 9 6 0 12
 * 10 4 8 0
 * 1
 * 
 * 
 * @author parveenchahal
 */

public class TravelingSalesPerson extends CodeTemplates{
    
    public static void readInputs() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] NM = toIntArrFromStringArr(br.readLine().split(" "));
        int[][] distArr = new int[NM[0]][NM[1]];
        for (int i = 0; i < NM[0]; i++) {
            for (int j = 0; j < NM[1]; j++) {
                for (int k : toIntArrFromStringArr(br.readLine().split(" "))) {
                    distArr[i][j++] = k;
                }
            }
        }
        int src = Integer.parseInt(br.readLine());
        for (int[] a : distArr) {
            for (int b : a) {
                System.out.print(b + "\t");
            }
            System.out.println();
        }
        getPath(distArr, src);
    }
    
    public static void getPath(int[][] distArr, int src) {
        distArr = getSquareArr(distArr);
        List<Node> pathSetArr = getSetPathArr(getArr0ToN(distArr.length, src), src);
        for (Node node : pathSetArr) {
            setMinDistance(pathSetArr, distArr, node, src);
        }
        for (Node node : pathSetArr) {
            System.out.println(node);
        }
    }
    
    private static List<Node> getSetPathArr(int[] arr, int src) {
        final List<Set<Integer>> allSets = PowerSet.get(arr);
        List<Node> pathSetArr = new ArrayList<>();
        for (Set<Integer> set : allSets) {
            for (int x : arr) {
                if (!set.contains(x)) {
                    pathSetArr.add(new Node(x, set));
                }
            }
        }
        pathSetArr.add(new Node(src, allSets.get(allSets.size() - 1)));
        Collections.sort(pathSetArr);
        return pathSetArr;
    }
    
    private static int[][] getSquareArr(int[][] distArr) {
        int maxSize = Math.max(distArr.length, distArr.length > 0 ? distArr[0].length : distArr.length);
        int[][] newDisArr = new int[maxSize][maxSize];
        for (int i = 0; i < maxSize; i++) {
            for (int j = 0; j < maxSize; j++) {
                if (i < distArr.length && j < distArr[i].length) {
                    newDisArr[i][j] = distArr[i][j];
                } else {
                    newDisArr[i][j] = -1;
                }
            }
        }
        return newDisArr;
    }
    
    private static int[] getArr0ToN(int n, int src) {
        int[] arr = new int[n - 1];
        int i = 0;
        for (int k = 0; k < n; k++) {
            if (k != src) {
                arr[i++] = k;
            }
        }
        return arr;
    }

    private static int distanceOf(List<Node> list, Node node) {
        for (Node x : list) {
            if (x.equals(node)) {
                return x.distance;
            }
        }
        return -1;
    }
    
    private static void setMinDistance(List<Node> list, int[][] distArr, Node node, int src) {
        if (node.viaSet.isEmpty()) {
            node.distance = distArr[src][node.currIndex];
            node.parent = src;
            return;
        }
        for (Integer x : node.viaSet) {
            Node tempNode = new Node(node);
            tempNode.viaSet.remove(x);
            tempNode.currIndex = x;
            int dis = distanceOf(list, tempNode) + distArr[x][node.currIndex];
            if (dis != -1 && (node.distance == -1 || dis < node.distance)) {
                node.distance = dis;
                node.parent = x;
            }
        }
    }
    
    private static class Node implements Comparable<Node> {

        int currIndex, parent, distance;
        Set<Integer> viaSet;

        public Node(int currIndex, Set<Integer> viaSet) {
            this.currIndex = currIndex;
            this.parent = -1;
            this.distance = -1;
            this.viaSet = viaSet;
        }

        public Node(Node node) {
            this.currIndex = node.currIndex;
            this.parent = node.parent;
            this.distance = node.distance;
            this.viaSet = new HashSet<>(node.viaSet);
        }

        @Override
        public boolean equals(Object obj) {
            if (this == obj) {
                return true;
            }
            if (obj == null) {
                return false;
            }
            if (getClass() != obj.getClass()) {
                return false;
            }
            final Node other = (Node) obj;
            if (this.currIndex != other.currIndex) {
                return false;
            }
            for (Integer x : this.viaSet) {
                if(!other.viaSet.contains(x)) {
                    return false;
                }
            }
            for (Integer x : other.viaSet) {
                if(!this.viaSet.contains(x)) {
                    return false;
                }
            }
            return true;
        }

        @Override
        public String toString() {
            return "{(" + currIndex + ", " + viaSet.toString() + ") -> D: " + distance + ", P:" + parent + "}";
        }

        @Override
        public int compareTo(Node o) {
            if (this.viaSet.size() != o.viaSet.size()) {
                return this.viaSet.size() - o.viaSet.size();
            }
            return this.currIndex - o.currIndex;
        }

    }
    
}
