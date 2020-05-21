def gemstones(arr):
  return len(set.intersection(*[set(a) for a in arr]))