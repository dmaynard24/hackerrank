def array_manipulation(n, queries):
  arr = [0] * n
  for query in queries:
    [a, b, k] = query
    arr[a - 1] += k
    if b < len(arr):
      arr[b] -= k

  max_slope = arr[0]
  running_slope = arr[0]
  for i in range(1, len(arr)):
    running_slope += arr[i]
    max_slope = max(max_slope, running_slope)

  return max_slope
