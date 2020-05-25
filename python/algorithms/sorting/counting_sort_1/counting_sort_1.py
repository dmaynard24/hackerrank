def counting_sort_1(arr):
  counts = [0] * 100
  for num in arr:
    counts[num] += 1
  return counts