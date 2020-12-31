// https://www.interviewbit.com/problems/first-missing-integer/

import java.util.*;
import java.util.function.Predicate;
import java.util.stream.Collectors;

public class FirstMissingInteger {

    static private void swap(List<Integer> A, int i, int j) {
        int t = A.get(i);
        A.set(i, A.get(j));
        A.set(j, t);
    }

    public int firstMissingPositive1(List<Integer> A) {
        int i = 0;
        int n = A.size();

        while(i < n) {
            if(A.get(i) - 1 != i
                && A.get(i) > 0
                && A.get(i) < n
                && A.get(i) != A.get(A.get(i) - 1)) {
                
                swap(A, i, A.get(i) - 1);
            } else {
                i++;
            }
        }
        for(i = 0; i < n; i++) {
            if(A.get(i) - 1 != i) {
                return i + 1;
            }
        }
        return A.size() + 1;
    }

    public int firstMissingPositive2(List<Integer> A) {
        A = A.stream().filter(new Predicate<Integer>(){
			@Override
			public boolean test(Integer arg0) {
				return arg0 >= 0;
			}
        }).collect(Collectors.toList());
        PriorityQueue<Integer> pq = new PriorityQueue<>(A);
        int curr = 0;
        while(pq.size() > 0) {
            int x = pq.poll();
            if(x - curr > 1) {
                break;
            }
            curr = x;
        }
        return curr + 1;
    }

    public static void main(String[] args) {
        ArrayList<Integer> x = new ArrayList<>();
        x.add(1);
        // x.add(1);
        // x.add(1);
        // x.add(1);
        // x.add(1);
        int t = new FirstMissingInteger().firstMissingPositive1(x);
        CodeTemplates.println(t);
    }
}
