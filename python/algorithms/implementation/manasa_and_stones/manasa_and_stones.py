def manasa_and_stones(n, a, b):
  if a == b:
    return [(n - 2) * a + b]
  return sorted([(n - i - 1) * a + i * b for i in range(n)])
