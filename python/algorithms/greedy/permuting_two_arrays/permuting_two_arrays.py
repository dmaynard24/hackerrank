def permuting_two_arrays(k, a, b):
  a.sort(reverse=True)
  b.sort()
  for i in range(len(b)):
    if a[i] + b[i] < k:
      return 'NO'
  return 'YES'