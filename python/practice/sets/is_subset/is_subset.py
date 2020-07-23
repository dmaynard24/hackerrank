def is_subset(a, b):
  a, b = set(a), set(b)
  return len(a) == len(a.intersection(b))