def utopian_tree(n):
  h = 1
  for i in range(n):
    if i % 2 == 0:
      h *= 2
    else:
      h += 1
  return h