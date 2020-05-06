def jumping_on_clouds_revisited(c, k):
  n = len(c)
  e = 100
  i = k
  e -= 3 if c[i] == 1 else 1
  while i != 0:
    i = (i + k) % n
    e -= 3 if c[i] == 1 else 1
  return e
