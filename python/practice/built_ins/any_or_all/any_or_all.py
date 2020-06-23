def any_or_all(arr):
  return all([int(a) > 0 for a in arr]) and any([a == a[::-1] for a in arr])