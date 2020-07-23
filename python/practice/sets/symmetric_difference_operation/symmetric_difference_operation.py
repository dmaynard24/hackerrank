def symmetric_difference_operation(a, b):
  a, b = set(a), set(b)
  return len(a.symmetric_difference(b))