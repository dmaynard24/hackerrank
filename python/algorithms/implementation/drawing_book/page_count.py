def page_count(n, p):
  if p == 1 or p == n:
    return 0
  if n % 2 == 0:
    return min(p // 2, (n - p + 1) // 2)
  else:
    return min(p // 2, (n - p) // 2)