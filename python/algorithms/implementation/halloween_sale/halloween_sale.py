def halloween_sale(p, d, m, s):
  count = 0
  while s - p >= 0:
    s -= p
    p -= d
    if p <= m:
      p = m
    count += 1
  return count