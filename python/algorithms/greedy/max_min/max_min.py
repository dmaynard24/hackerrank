def max_min(k, arr):
  arr.sort()

  min_diff = arr[-1]
  for i in range(len(arr) - (k - 1)):
    min_diff = min(min_diff, arr[i + k - 1] - arr[i])

  return min_diff
