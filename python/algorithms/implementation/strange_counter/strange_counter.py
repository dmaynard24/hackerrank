def strange_counter(t):
  start = 3
  total = start
  while total < t:
    start *= 2
    total += start
  return total - t + 1