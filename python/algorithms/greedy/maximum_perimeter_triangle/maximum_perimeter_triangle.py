def maximum_perimeter_triangle(sticks):
  sticks.sort()
  max_p = 0
  max_tri = []
  for a in range(len(sticks)):
    for b in range(a + 1, len(sticks)):
      for c in range(b + 1, len(sticks)):
        if sticks[a] + sticks[b] > sticks[c]:
          p = sticks[a] + sticks[b] + sticks[c]
          if p > max_p:
            max_p = p
            max_tri = [sticks[a], sticks[b], sticks[c]]
          elif p == max_p:
            if c > max_tri[2]:
              max_tri = [sticks[a], sticks[b], sticks[c]]
            elif c == max_tri[2]:
              if a < max_tri[0]:
                max_tri = [sticks[a], sticks[b], sticks[c]]
  return max_tri if max_p != 0 else [-1]