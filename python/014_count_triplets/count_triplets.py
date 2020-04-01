def count_triplets(arr, r):
  count = 0
  val_counts = {}
  pair_counts = {}

  for i in range(len(arr) - 1, -1, -1):
    val = arr[i]
    # first term in a triple (increase total count)
    if val * r in pair_counts:
      count += pair_counts[val * r]
    # middle term in a triple (increase pair count)
    if val * r in val_counts:
      pair_counts[val] = pair_counts.get(val, 0) + val_counts[val * r]

    # all counts
    val_counts[val] = val_counts.get(val, 0) + 1

  return count


print(count_triplets([1, 2, 2, 4], 2))  # 2
print(count_triplets([1, 3, 9, 9, 27, 81], 3))  # 6
print(count_triplets([1, 5, 5, 25, 125], 5))  # 4
print(
    count_triplets([
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1
    ], 1))  # 161700
