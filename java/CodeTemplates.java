import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.security.InvalidParameterException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.LinkedList;

//==============================================================================================================================
//Template
//==============================================================================================================================
public class CodeTemplates {

//==============================================================================================================================
//Constants
//==============================================================================================================================
    public static int MOD = ((int) 1e9 + 7);
    public static double PI = Math.PI;
    public static Comparator<Integer> reverseIntegerComparator = (Integer o1, Integer o2) -> o2 - o1;
    public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

//==============================================================================================================================
//Input/Output methods
//==============================================================================================================================
    public static int readIntegerFromLine() throws IOException {
        return Integer.parseInt(br.readLine());
    }

    public static long readLongFromLine() throws IOException {
        return Long.parseLong(br.readLine());
    }

    public static double readDoubleFromLine() throws IOException {
        return Double.parseDouble(br.readLine());
    }

    public static int[] readIntegerArrayFromLine() throws IOException {
        return toIntArrFromStringArr(br.readLine().split(" "));
    }

    public static long[] readLongArrayFromLine() throws IOException {
        return toLongArrFromStringArr(br.readLine().split(" "));
    }

    public static double[] readDoubleArrayFromLine() throws IOException {
        return toDoubleArrFromStringArr(br.readLine().split(" "));
    }

    public static String readLineFromLine() throws IOException {
        return br.readLine();
    }

    public static int[] toIntArrFromStringArr(String[] arr) {
        return Arrays.stream(arr).mapToInt(Integer::parseInt).toArray();
    }

    public static long[] toLongArrFromStringArr(String[] arr) {
        return Arrays.stream(arr).mapToLong(Long::parseLong).toArray();
    }

    public static double[] toDoubleArrFromStringArr(String[] arr) {
        return Arrays.stream(arr).mapToDouble(Double::parseDouble).toArray();
    }

    public static void println(Object... obj) {
        String x = "";
        for (Object o : obj) {
            if (o != null) {
                x += o.toString() + ", ";
            } else {
                x += "null, ";
            }
        }
        if (x.length() > 0) {
            System.out.println(x.substring(0, x.length() - 2));
        } else {
            System.out.println(x);
        }
    }

    public static void printArray(int[] arr) {
        System.out.print(Arrays.toString(arr));
    }

    public static void printArray(char[] arr) {
        System.out.print(Arrays.toString(arr));
    }

    public static void printArray(long[] arr) {
        System.out.print(Arrays.toString(arr));
    }

    public static void printArray(double[] arr) {
        System.out.print(Arrays.toString(arr));
    }

    public static void printMatrix(List<List<? extends Object>> matrix) {
        for(List<? extends Object> list : matrix) {
            for (Object x : list) {
                System.out.print(x.toString() + "\t");
            }
            System.out.println();
        }
    }

    public static void printMatrix(int[][] matrix) {
        for (int[] col : matrix) {
            for (int x : col) {
                System.out.print(x + "\t");
            }
            System.out.println();
        }
    }

    public static void printMatrix(long[][] matrix) {
        for (long[] col : matrix) {
            for (long x : col) {
                System.out.print(x + "\t");
            }
            System.out.println();
        }
    }

    public static void printMatrix(char[][] matrix) {
        for (char[] col : matrix) {
            for (char x : col) {
                System.out.print(x + "\t");
            }
            System.out.println();
        }
    }

//==============================================================================================================================
//Max/Min methods
//==============================================================================================================================
    public static int max(int[] arr) {
        return Arrays.stream(arr).max().getAsInt();
    }

    public static int min(int[] arr) {
        return Arrays.stream(arr).min().getAsInt();
    }

    public static long max(long[] arr) {
        return Arrays.stream(arr).max().getAsLong();
    }

    public static long min(long[] arr) {
        return Arrays.stream(arr).min().getAsLong();
    }

    public static double max(double[] arr) {
        return Arrays.stream(arr).max().getAsDouble();
    }

    public static double min(double[] arr) {
        return Arrays.stream(arr).min().getAsDouble();
    }

    public static double max(double a, double b, double c) {
        return Math.max(a, Math.max(b, c));
    }

    public static double min(double a, double b, double c) {
        return Math.min(a, Math.min(b, c));
    }

//==============================================================================================================================
//Reverse methods
//==============================================================================================================================
    public static void reverse(List<?> list) {
        Collections.sort(list, Collections.reverseOrder());
    }

    public static void reverse(int[] arr) {
        int N = arr.length;
        int lastIndex = N - 1;
        int half = N / 2;
        for (int i = 0; i < half; i++) {
            int t = arr[i];
            arr[i] = arr[lastIndex - i];
            arr[lastIndex - i] = t;
        }
    }

    public static void reverse(long[] arr) {
        int N = arr.length;
        int lastIndex = N - 1;
        int half = N / 2;
        for (int i = 0; i < half; i++) {
            long t = arr[i];
            arr[i] = arr[lastIndex - i];
            arr[lastIndex - i] = t;
        }
    }

    public static void reverse(double[] arr) {
        int N = arr.length;
        int lastIndex = N - 1;
        int half = N / 2;
        for (int i = 0; i < half; i++) {
            double t = arr[i];
            arr[i] = arr[lastIndex - i];
            arr[lastIndex - i] = t;
        }
    }

    public static void reverse(char[] arr) {
        int N = arr.length;
        int lastIndex = N - 1;
        int half = N / 2;
        for (int i = 0; i < half; i++) {
            char t = arr[i];
            arr[i] = arr[lastIndex - i];
            arr[lastIndex - i] = t;
        }
    }

    public static String reverse(String str) {
        char[] charArr = str.toCharArray();
        reverse(charArr);
        StringBuilder sb = new StringBuilder();
        for (char c : charArr) {
            sb.append(c);
        }
        return sb.toString();
    }

//==============================================================================================================================
//Maths methods
//==============================================================================================================================
    public static double logNWithBase(double N, double base) {
        return Math.log(N) / Math.log(base);
    }

    public static String factorial(int n) {
        if (n >= 0) {
            BigInteger one = new BigInteger("1");
            BigInteger N = new BigInteger(Integer.toString(n));
            BigInteger factorial = new BigInteger(N.toString());
            N = N.subtract(one);
            while (N.compareTo(one) > 0) {
                factorial = factorial.multiply(N);
                N = N.subtract(one);
            }
            return factorial.toString();
        } else {
            throw new InvalidParameterException("n should be greater than equal to 0");
        }
    }

    public static String nCr(int n, int r) {
        if (n >= r && r > 0) {
            return new BigInteger(nPr(n, r)).divide(new BigInteger(factorial(r))).toString();
        } else {
            throw new InvalidParameterException("n and r should be positive and n should be greater than equal to r");
        }

    }

    public static String nPr(int n, int r) {
        if (n >= r && r > 0) {
            return new BigInteger(factorial(n)).divide(new BigInteger(factorial(n - r))).toString();
        } else {
            throw new InvalidParameterException("n and r should be positive and n should be greater than equal to r");
        }
    }

    public static int gcd(int a, int b) {
        if (a == 0 || b == 0) {
            return 0;
        }
        if (a == b) {
            return a;
        }
        if (a > b) {
            return gcd(a - b, b);
        }
        return gcd(a, b - a);
    }

    public static long lcm(int[] arr) {
        long lcm = 1;
        int divisor = 2;

        while (true) {
            int counter = 0;
            boolean divisible = false;

            for (int i = 0; i < arr.length; i++) {
                if (arr[i] == 0) {
                    return 0;
                } else if (arr[i] < 0) {
                    arr[i] = arr[i] * (-1);
                }
                if (arr[i] == 1) {
                    counter++;
                }
                if (arr[i] % divisor == 0) {
                    divisible = true;
                    arr[i] = arr[i] / divisor;
                }
            }
            if (divisible) {
                lcm = lcm * divisor;
            } else {
                divisor++;
            }
            if (counter == arr.length) {
                return lcm;
            }
        }
    }

//==============================================================================================================================
//Classes
//==============================================================================================================================
    public static class Queue<E> extends LinkedList<E> {

        public Queue() {
        }

        public void enqueue(E value) {
            add(value);
        }

        public E dequeue() {
            if (size() <= 0) {
                return null;
            }
            return pollFirst();
        }

    }

    public static class PowerSet {

        public static List<Set<Integer>> get(int[] arr) {
            long nSets = 0;
            int N = arr.length;
            for (int i = 0; i < N; i++) {
                nSets = (nSets << 1) | 1;
            }
            ArrayList<Set<Integer>> result = new ArrayList<>();
            result.add(new HashSet<>());
            for (long i = 1; i <= nSets; i++) {
                Set<Integer> s = new HashSet<>();
                long p = i;
                for (int j = 0; p > 0; j++, p >>>= 1) {
                    if ((p & 1) > 0) {
                        s.add(arr[j]);
                    }
                }
                result.add(s);
            }
            return result;
        }

        public static <T extends Object> List<Set<T>> get(T[] arr) {
            long nSets = 0;
            int N = arr.length;
            for (int i = 0; i < N; i++) {
                nSets = (nSets << 1) | 1;
            }
            ArrayList<Set<T>> result = new ArrayList<>();
            result.add(new HashSet<>());
            for (long i = 1; i <= nSets; i++) {
                Set<T> s = new HashSet<>();
                long p = i;
                for (int j = 0; p > 0; j++, p >>>= 1) {
                    if ((p & 1) > 0) {
                        s.add(arr[j]);
                    }
                }
                result.add(s);
            }
            return result;
        }
    }

    public static class Point<E> {

        private E x;
        private E y;

        public Point(E x, E y) {
            this.x = x;
            this.y = y;
        }

        public E getX() {
            return x;
        }

        public void setX(E x) {
            this.x = x;
        }

        public E getY() {
            return y;
        }

        public void setY(E y) {
            this.y = y;
        }

        @Override
        public String toString() {
            return "(x : " + this.x + ", y : " + this.y + ")";
        }
    }

    public static class Graph<E, P> {

        private Map<E, List<Edge<E, P>>> map;

        static public class Edge<E, P> {

            private E u, v;
            private P param;

            public E getU() {
                return u;
            }

            public E getV() {
                return v;
            }

            public P getParams() {
                return param;
            }

            public Edge(E u, E v, P params) {
                this.u = u;
                this.v = v;
                this.param = params;
            }

            public Edge(Edge<E, P> edge) {
                this.u = edge.u;
                this.v = edge.v;
                this.param = edge.param;
            }

            public Edge(Edge<E, P> edge, P params) {
                this.u = edge.u;
                this.v = edge.v;
                this.param = params;
            }

            @Override
            public String toString() {
                return "{u=" + u.toString() + ", v=" + v.toString() + ", param=" + param.toString() + "}";
            }
        }

        public Graph() {
            map = new HashMap<>();
        }

        @Override
        public String toString() {
            return map.toString();
        }

        public void addEdge(Edge<E, P> edge) {
            List<Edge<E, P>> list = map.get(edge.u);
            if (list != null) {
                list.add(edge);
            } else {
                list = new ArrayList<>();
                list.add(edge);
                map.put(edge.u, list);
            }
        }

        public List<Edge<E, P>> getConnections(E u) {
            return map.get(u);
        }

        public void reverseAllDirections() {
            Graph<E, P> newGraph = new Graph();
            for (Map.Entry<E, List<Edge<E, P>>> entry : map.entrySet()) {
                List<Graph.Edge<E, P>> list = entry.getValue();
                list.forEach((edge) -> {
                    newGraph.addEdge(new Edge(edge.v, edge.u, edge.param));
                });
            }
            this.map = newGraph.map;
        }
    }

}
