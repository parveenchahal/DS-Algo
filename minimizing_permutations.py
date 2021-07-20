# https://leetcode.com/discuss/interview-question/1137426/Facebook-or-Minimizing-Permutations


def minOperations(arr):
  n = len(arr)
  s = ''.join(map(str, arr))
  target = ''.join(sorted(s))
  q = deque()
  q.append((s, 0))
  visited = set([s])
  while len(q) > 0:
    x, d = q.popleft()
    if x == target:
      return d
    for k in range(2, n + 1):
      for i in range(0, n - k + 1):
        j = i + k
        c = x
        c = c[:i] + c[i:j][::-1] + c[j:]
        if c not in visited:
          visited.add(c)
          q.append((c, d + 1))
  return -1
