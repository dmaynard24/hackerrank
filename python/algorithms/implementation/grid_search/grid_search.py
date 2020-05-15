def grid_search(g, p):
  for i in range(len(g) - len(p) + 1):
    index = g[i].find(p[0], 0)
    while index > -1:
      for j in range(1, len(p)):
        if g[i + j][index:index + len(p[j])] != p[j]:
          break
        elif j == len(p) - 1:
          return 'YES'
      # look for next index in same string
      index = g[i].find(p[0], index + 1)
  return 'NO'