def beautiful_triplets(d, arr):
  count = 0
  for i in range(len(arr) - 2):
    for j in range(i + 1, len(arr) - 1):
      if arr[j] - arr[i] > d:
        break
      if arr[j] - arr[i] == d:
        for k in range(j + 1, len(arr)):
          if arr[k] - arr[j] > d:
            break
          if arr[k] - arr[j] == d:
            count += 1
  return count