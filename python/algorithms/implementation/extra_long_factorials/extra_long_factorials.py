def extra_long_factorials(n):
  factorial = 1
  while n > 1:
    factorial *= n
    n -= 1
  return factorial