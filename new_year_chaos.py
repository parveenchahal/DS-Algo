def merge(arr, l, mid, r):
    i = l
    j = mid + 1
    temp_list = []
    inv = 0
    while i <= mid and j <= r:
        if arr[i] <= arr[j]:
            temp_list.append(arr[i])
            i += 1
        else:
            inv += mid - i + 1
            temp_list.append(arr[j])
            j += 1
    if i <= mid:
        for k in range(i, mid + 1):
            temp_list.append(arr[k])
    if j <= r:
        for k in range(j, r + 1):
            temp_list.append(arr[k])
    for k in range(l, r + 1):
        arr[k] = temp_list.pop(0)
    return inv

def merge_sort(arr, l, r):
    inv = 0
    if l < r:
        mid = (l + r) // 2
        inv = merge_sort(arr, l, mid)
        inv += merge_sort(arr, mid + 1, r)
        inv += merge(arr, l, mid, r)
    return inv

def minimum_bribes(q):
    n = len(q)
    for i in range(n):
        x = q[i] - i - 1
        if x > 2:
            return "Too chaotic"
    inv = merge_sort(q, 0, n - 1)
    return inv

minimum_bribes()

# t = int(input())
# for _ in range(t):
#     n = int(input())
#     q = list(map(int, input().rstrip().split()))
#     r = minimum_bribes(q)
#     print(r)