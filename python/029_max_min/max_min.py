def maxMin(k, arr):
  arr.sort()

  min_diff = arr[-1]
  for i in range(len(arr) - (k - 1)):
    min_diff = min(min_diff, arr[i + k - 1] - arr[i])

  return min_diff


print(maxMin(3, [10, 100, 300, 200, 1_000, 20, 30]))  # 20
print(maxMin(4, [1, 2, 3, 4, 10, 20, 30, 40, 100, 200]))  # 3
print(maxMin(2, [1, 2, 1, 2, 1]))  # 0
