def countTriplets(arr, r):
  count = 0
  val_counts = {}
  pair_counts = {}

  for i in range(len(arr) - 1, -1, -1):
    # first term in a triple (increase total count)
    if arr[i] * r in pair_counts:
      count += pair_counts[arr[i] * r]
    # middle term in a triple (increase pair count)
    if arr[i] * r in val_counts:
      pair_counts[arr[i]] = pair_counts.get(arr[i], 0) + val_counts[arr[i] * r]

    # all counts
    val_counts[arr[i]] = val_counts.get(arr[i], 0) + 1

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
