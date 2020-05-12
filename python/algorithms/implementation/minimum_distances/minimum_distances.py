def minimum_distances(a):
  l = len(a)
  md = l * 2
  indices = {}
  for i, num in enumerate(a):
    if num in indices:
      md = min(md, i - indices.get(num))
    indices[num] = i
  return md if md != l * 2 else -1