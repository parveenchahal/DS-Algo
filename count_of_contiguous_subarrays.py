# https://leetcode.com/discuss/interview-question/742523/facebook-prep-question-contiguous-subarrays-on-solution

def count_subarrays(arr):
  n = len(arr)
  res = [1] * n
  st = []
  for i in range(n):
    while len(st) > 0 and arr[st[-1]] < arr[i]:
      st.pop()
    res[i] += (i - 1 - st[-1]) if len(st) > 0 else i
    st.append(i)
  
  st = []
  for i in range(n - 1, -1, -1):
    while len(st) > 0 and arr[st[-1]] < arr[i]:
      st.pop()
    res[i] += (st[-1] - 1 - i) if len(st) > 0 else n - 1 - i
    st.append(i)
  return res
