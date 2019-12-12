package DSAlgo;
import java.util.*;

/**
 *
 * @author parveenchahal
 * @param <E>
 */
public class HeapMap<E> {

    final private Map<E, Integer> map;

    final private List<E> list;

    private final Comparator<? super E> comparator;

    @Override
    public String toString() {
        return list.toString() + "\n" + map.toString();
    }

    public HeapMap() {
        this.list = new ArrayList<>();
        this.comparator = null;
        this.map = new HashMap<>();
    }

    public HeapMap(Comparator<? super E> comparator) {
        this.list = new ArrayList<>();
        this.comparator = comparator;
        this.map = new HashMap<>();
    }

    public int size() {
        return list.size();
    }

    public boolean isEmpty() {
        return size() <= 0;
    }

    public void insert(E e) {
        if (e != null) {
            list.add(e);
            siftUp(list.size() - 1);
        }
    }

    public boolean contains(E e) {
        return map.containsKey(e);
    }

    public E remove() {
        if (list.size() <= 0) {
            return null;
        }
        E removedElement = list.get(0);
        map.remove(removedElement);
        E lastElement = list.remove(list.size() - 1);
        if (list.size() > 0) {
            list.set(0, lastElement);
            siftDown(0);
        }
        return (E) removedElement;
    }

    public void change(E oldE, E newE) {
        try {
            Integer index = map.get(oldE);
            if (index != null) {
                map.remove(oldE);
                change(index, newE);
            } else {
                throw new Exception("Object not found in HashMap");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private void change(int index, E newE) {
        int cmp = compare(newE, list.get(index));
        list.set(index, newE);
        if (cmp < 0) {
            siftUp(index);
        } else if (cmp > 0) {
            siftDown(index);
        }
    }

    private int compare(E e1, E e2) {
        if (comparator != null) {
            return comparator.compare(e1, e2);
        }
        Comparable<? super E> key = (Comparable<? super E>) e1;
        return key.compareTo(e2);
    }

    private static int iParent(int index) {
        return (index - 1) >>> 1;
    }

    private static int iLeftChild(int index) {
        return (index << 1) + 1;
    }

    private static int iRightChild(int index) {
        return (index << 1) + 2;
    }

    private void siftUp(int index) {
        E temp = list.get(index);
        while (index > 0) {
            int parent = iParent(index);
            if (compare(temp, list.get(parent)) >= 0) {
                break;
            }
            list.set(index, list.get(parent));
            map.put(list.get(parent), index);
            index = parent;
        }
        list.set(index, temp);
        map.put(temp, index);
    }

    private void siftDown(int index) {
        if (list.size() < 2) {
            return;
        }
        int lastParent = iParent(list.size() - 1);
        E temp = list.get(index);
        while (index <= lastParent) {
            int childIndex = iLeftChild(index);
            E child = (E) list.get(childIndex);
            int rightIndex = iRightChild(index);
            if (rightIndex < list.size() && compare(child, list.get(rightIndex)) > 0) {
                child = list.get(rightIndex);
                childIndex = rightIndex;
            }
            if (compare((E) temp, child) <= 0) {
                break;
            }
            list.set(index, child);
            map.put(child, index);
            index = childIndex;
        }
        list.set(index, temp);
        map.put(temp, index);
    }

    private void heapify() {
        for (int i = iParent(list.size() - 1); i >= 0; i--) {
            siftDown(i);
        }
    }
}
