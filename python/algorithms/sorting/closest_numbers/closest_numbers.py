def closest_numbers(arr):
  arr.sort()
  min_diff = abs(arr[1] - arr[0])
  min_pairs = [arr[0], arr[1]]
  for i in range(2, len(arr)):
    diff = abs(arr[i] - arr[i - 1])
    if diff < min_diff:
      min_diff = diff
      min_pairs = [arr[i - 1], arr[i]]
    elif diff == min_diff:
      min_pairs.extend([arr[i - 1], arr[i]])
  return min_pairs