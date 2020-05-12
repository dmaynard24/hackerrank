def minimum_distances(a):
  l = len(a)
  md = l * 2
  indices = {num: [] for num in a}
  for i, num in enumerate(a):
    indices[num].append(i)
  for v in indices.values():
    if len(v) < 2:
      continue
    for i in range(1, len(v)):
      md = min(md, v[i] - v[i - 1])
  return md if md != l * 2 else -1