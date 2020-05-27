def priyanka_and_toys(w):
  w.sort()
  count = 1
  min_weight = w[0]
  for i in range(len(w)):
    if w[i] > min_weight + 4:
      count += 1
      min_weight = w[i]
  return count