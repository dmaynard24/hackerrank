def minimumAbsoluteDifference(arr):
  arr.sort()
  minimum = abs(arr[0] - arr[1])
  for i in range(1, len(arr)):
    minimum = min(minimum, abs(arr[i - 1] - arr[i]))

  return minimum


print(minimumAbsoluteDifference([3, -7, 0]))  # 3
print(minimumAbsoluteDifference([-59, -36, -13, 1, -53, -92, -2, -96, -54,
                                 75]))  # 1
print(minimumAbsoluteDifference([1, -3, 71, 68, 17]))  # 3
