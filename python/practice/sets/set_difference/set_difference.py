def set_difference(a, b):
  a, b = set(a), set(b)
  return len(a.difference(b))