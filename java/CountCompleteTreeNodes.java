/**
 * Leetcode- https://leetcode.com/problems/count-complete-tree-nodes
 *
 * @author parveenchahal
 */
/**
 * Used binary search on last level of tree First get the path how will it look
 * like for 5 it is- 1, 2, 5 for 7 it is- 1, 3, 7 parent of any number would be
 * num/2 and then check if path is valid or not if num is even go to left
 * otherwise go to right in the tree
 *
 */

import java.util.*;

class CountCompleteTreeNodes1 {

    class TreeNode {

        TreeNode left, right;
    }

    private int leftHeightOfTree(TreeNode root) {
        int height = 0;
        while (root != null) {
            root = root.left;
            height++;
        }
        return height;
    }
    
    private int rightHeightOfTree(TreeNode root) {
        int height = 0;
        while (root != null) {
            root = root.right;
            height++;
        }
        return height;
    }

    private Stack<Integer> getPathOf(int num) {
        Stack<Integer> st = new Stack<>();
        while (num > 0) {
            st.push(num);
            num >>>= 1;
        }
        return st;
    }

    public int countNodes(TreeNode root) {
        int leftHeight = leftHeightOfTree(root);
        int rightHeight = rightHeightOfTree(root);
        if (leftHeight == rightHeight) {
            return (1 << leftHeight) - 1;
        }
        return 1 + countNodes(root.left) + countNodes(root.right);
    }
}


class CountCompleteTreeNodes2 {

    class TreeNode {

        TreeNode left, right;
    }

    private int heightOfTree(TreeNode root) {
        int height = 0;
        while (root != null) {
            root = root.left;
            height++;
        }
        return height;
    }

    private boolean isValidPath(TreeNode root, Stack<Integer> st) {

        if (st.size() > 0) {
            st.pop();
        }

        while (root != null && st.size() > 0) {
            //if peek is even number
            if ((st.peek() & 1) == 0) {
                root = root.left;
            } else {
                root = root.right;
            }
            st.pop();
        }
        return st.size() <= 0 && root != null;
    }

    private Stack<Integer> getPathOf(int num) {
        Stack<Integer> st = new Stack<>();
        while (num > 0) {
            st.push(num);
            num >>>= 1;
        }
        return st;
    }

    public int countNodes(TreeNode root) {
        int height = heightOfTree(root);
        int l = (int) Math.pow(2, height - 1);
        int r = (int) (Math.pow(2, height) - 1);
        int result = 0;
        while (l <= r) {
            int mid = (l + r) / 2;
            Stack<Integer> st = getPathOf(mid);
            if (isValidPath(root, st)) {
                result = mid;
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return result;
    }
}
