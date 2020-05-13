def flatland_space_stations(n, c):
  c.sort()
  md = 0
  if c[0] != 0:
    md = max(md, c[0] - 0)
  for i in range(1, len(c)):
    md = max(md, (c[i] - c[i - 1]) // 2)
  if c[-1] != n - 1:
    md = max(md, (n - 1) - c[-1])
  return md