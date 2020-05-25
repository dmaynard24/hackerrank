def counting_sort_2(arr):
  counts = [0] * 100
  for num in arr:
    counts[num] += 1
  sorted_arr = []
  for i, count in enumerate(counts):
    sorted_arr.extend([i] * count)
  return sorted_arr