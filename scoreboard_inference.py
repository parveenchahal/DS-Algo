def getMinProblemCount(N: int, S: List[int]) -> int:
    have_odd = False
    ma = S[0]
    for x in S:
      if not have_odd and (x & 1) == 1:
        have_odd = True
      ma = max(ma, x)
    if (ma & 1) == 1:
      return ((ma - 1) // 2) + 1
    return (ma // 2) + (1 if have_odd else 0)
