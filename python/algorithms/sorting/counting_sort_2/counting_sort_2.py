def counting_sort_2(arr):
  counts = [0] * 100
  for num in arr:
    counts[num] += 1

  i = 0
  for j in range(len(counts)):
    count = counts[j]
    arr[i:i + count] = [j] * count
    i += count

  return arr
