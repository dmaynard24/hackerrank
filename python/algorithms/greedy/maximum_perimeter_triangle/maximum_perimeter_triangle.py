def maximum_perimeter_triangle(sticks):
  sticks.sort()
  i = len(sticks) - 3
  while i >= 0:
    if sticks[i] + sticks[i + 1] > sticks[i + 2]:
      return [sticks[i], sticks[i + 1], sticks[i + 2]]
    i -= 1
  return [-1]