def chocolate_feast(n, c, m):
  bars = n // c
  wrappers = bars
  count = bars
  while wrappers >= m:
    bars = wrappers // m
    wrappers = wrappers % m + bars
    count += bars
  return count