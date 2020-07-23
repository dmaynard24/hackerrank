def symmetric_difference(a, b):
  a, b = set(a), set(b)
  return '\n'.join(
      map(str, sorted(set.union(a.difference(b), b.difference(a)), key=int)))
