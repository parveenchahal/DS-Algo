
import java.util.*;
/**
 *
 * @author parveenchahal
 * @param <K>
 * @param <V>
 */
public class AVLTree<K extends Comparable<K>, V> {

    private class Node implements Comparable<Node> {

        K key;
        V value;
        Node left, right;
        int size, height, BF;

        public Node(K key) {
            this(key, null);
        }

        public Node(K key, V value) {
            this.key = key;
            this.value = value;
            this.left = null;
            this.right = null;
            this.size = 1;
            this.height = 1;
            this.BF = 0;
        }

        @Override
        public int compareTo(Node o) {
            if (comparator != null) {
                return comparator.compare(key, o.key);
            }
            return key.compareTo(o.key);
        }

        @Override
        public String toString() {
            return "{Key: " + key.toString() + " ----> LC: " + (left != null ? left.key.toString() : "null") + ", RC: " + (right != null ? right.key.toString() : "null") + ", Height: " + height + ", BF: " + BF + ", Size: " + size + "}";
        }
    }

    private Node root;
    private Comparator comparator;

    public AVLTree() {
        this.root = null;
        this.comparator = null;
    }

    public AVLTree(Comparator<K> c) {
        this.root = null;
        this.comparator = c;
    }

    public boolean contains(K key) {
        return get(root, new Node(key, null)) != null;
    }

    public V get(K key) {
        Node node = get(root, new Node(key, null));
        if (node != null) {
            return node.value;
        }
        return null;
    }

    private Node get(Node root, Node key) {
        if (root == null) {
            return null;
        }
        int cmp = key.compareTo(root);
        if (cmp < 0) {
            return get(root.left, key);
        } else if (cmp > 0) {
            return get(root.right, key);
        }
        return root;
    }

    private int height(Node node) {
        if (node != null) {
            return node.height;
        }
        return 0;
    }

    private int size(Node node) {
        if (node != null) {
            return node.size;
        }
        return 0;
    }

    public void insert(K key) {
        insert(key, null);
    }

    public void insert(K key, V value) {
        if (key != null) {
            root = insert(root, new Node(key, value));
        }
    }

    private Node insert(Node root, Node newNode) {
        if (root == null) {
            return newNode;
        }
        int cmp = newNode.compareTo(root);
        if (cmp < 0) {
            root.left = insert(root.left, newNode);
        } else if (cmp > 0) {
            root.right = insert(root.right, newNode);
        } else {
            root.value = newNode.value;
        }
        resetHeightBfSize(root);
        return ifAffectedThenBalanceIt(root);
    }

    private Node ifAffectedThenBalanceIt(Node root) {
        if (root.BF > 1) {
            if (root.left.BF > 0) {
                root = rotateRight(root);
            } else {
                root.left = rotateLeft(root.left);
                root = rotateRight(root);
            }
        } else if (root.BF < -1) {
            if (root.right.BF < 0) {
                root = rotateLeft(root);
            } else {
                root.right = rotateRight(root.right);
                root = rotateLeft(root);
            }
        }
        return root;
    }

    private Node rotateRight(Node A) {
        Node B = A.left;
        Node C = B.right;
        A.left = C;
        B.right = A;
        resetHeightBfSize(A);
        resetHeightBfSize(B);
        return B;
    }

    private void resetHeightBfSize(Node node) {
        node.height = Math.max(height(node.left), height(node.right)) + 1;
        node.size = size(node.left) + size(node.right) + 1;
        node.BF = height(node.left) - height(node.right);
    }

    private Node rotateLeft(Node A) {
        Node B = A.right;
        Node C = B.left;
        A.right = C;
        B.left = A;
        resetHeightBfSize(A);
        resetHeightBfSize(B);
        return B;
    }

    public void preOrder() {
        preOrder(root);
    }

    private void preOrder(Node root) {
        if (root == null) {
            return;
        }
        System.out.println(root);
        preOrder(root.left);
        preOrder(root.right);
    }

    public void inOrder() {
        inOrder(root);
    }

    private void inOrder(Node root) {
        if (root == null) {
            return;
        }
        inOrder(root.left);
        System.out.println(root);
        inOrder(root.right);
    }

    public int size() {
        return size(root);
    }

    public int height() {
        return height(root);
    }

    public int rank(K key) {
        if (key != null) {
            return rank(root, new Node(key), 1);
        }
        return -1;
    }

    private int rank(Node root, Node key, int rank) {
        if (root == null) {
            return -1;
        }
        int cmp = key.compareTo(root);
        if (cmp < 0) {
            rank = rank(root.left, key, rank);
        } else if (cmp > 0) {
            rank = rank(root.right, key, rank + size(root.left) + 1);
        } else {
            return size(root.left) + rank;
        }
        return rank;
    }

}
