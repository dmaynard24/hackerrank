def jumping_on_clouds_revisited(c, k):
  n = len(c)
  e = 100
  i = 0
  while True:
    i = (i + k) % n
    e -= 3 if c[i] == 1 else 1
    if i == 0:
      break
  return e
