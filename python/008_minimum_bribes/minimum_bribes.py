

def minimum_bribes(q):
  total_bribe_count = 0
  for i in range(len(q) - 1, -1, -1):
    if q[i] - (i + 1) > 2:
      return 'Too chaotic'
    for j in range(max(0, q[i] - 2), i):
      if q[j] > q[i]:
        total_bribe_count += 1
  return total_bribe_count