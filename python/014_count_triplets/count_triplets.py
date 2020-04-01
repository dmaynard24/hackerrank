def countTriplets(arr, r):
  count = 0
  val_counts = {}
  for val in arr:
    if val in val_counts:
      val_counts[val] += 1
    else:
      val_counts[val] = 1
  for i in range(0, len(arr) - 2):
    if arr[i] * r in val_counts and arr[i] * r * r in val_counts:
      count += max(val_counts[arr[i] * r], val_counts[arr[i] * r * r])
  return count


print(countTriplets([1, 2, 2, 4], 2))  # 2
print(countTriplets([1, 3, 9, 9, 27, 81], 3))  # 6
print(countTriplets([1, 5, 5, 25, 125], 5))  # 4
print(
    countTriplets([
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1
    ], 1))  # 161700
