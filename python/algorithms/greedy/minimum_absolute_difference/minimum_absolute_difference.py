def minimum_absolute_difference(arr):
  arr.sort()
  minimum = abs(arr[0] - arr[1])
  for i in range(1, len(arr)):
    minimum = min(minimum, abs(arr[i - 1] - arr[i]))

  return minimum
