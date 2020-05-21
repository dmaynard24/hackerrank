def gemstones(arr):
  minerals = [set(a) for a in arr]
  shortest_i = 0
  shortest = len(minerals[0])
  for i in range(1, len(minerals)):
    if len(minerals[i]) < shortest:
      shortest_i = i
      shortest = len(minerals[i])
  count = 0
  for char in minerals[shortest_i]:
    is_gemstone = True
    for i, mineral in enumerate(minerals):
      if i == shortest_i:
        continue
      if char not in mineral:
        is_gemstone = False
        break
    if is_gemstone:
      count += 1
  return count