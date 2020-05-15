def gridSearch(G, P):
  for i in range(len(G) - len(P) + 1):
    index = G[i].find(P[0])
    if index == -1:
      continue
    for j in range(1, len(P)):
      if G[i + j][index:index + len(P[j])] != P[j]:
        break
      elif j == len(P) - 1:
        return 'YES'
  return 'NO'