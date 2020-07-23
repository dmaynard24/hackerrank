def set_symmetric_difference(a, b):
  a, b = set(a), set(b)
  return '\n'.join(map(str, sorted(a.symmetric_difference(b), key=int)))