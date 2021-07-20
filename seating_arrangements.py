# https://leetcode.com/discuss/interview-question/709517/facebook-recruiting-portal-seating-arrangements


def minOverallAwkwardness(arr):
  n = len(arr)
  arr.sort()
  dq = deque()
  dq.append(arr[0])
  alt_left = False
  for i in range(1, n):
    if alt_left:
      dq.appendleft(arr[i])
    else:
      dq.append(arr[i])
    alt_left = not alt_left
  res = abs(dq[0] - dq[-1])
  print
  for i in range(1, n):
    res = max(res, abs(dq[i] - dq[i - 1]))
  return res
