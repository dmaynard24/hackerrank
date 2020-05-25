def insertion_sort_1(n, arr):
  result = []
  val = arr[-1]
  i = len(arr) - 2
  while i > -1:
    if arr[i] > val:
      arr[i + 1] = arr[i]
      result.append(' '.join(map(str, arr)))
    else:
      arr[i + 1] = val
      result.append(' '.join(map(str, arr)))
      break
    i -= 1
  if i == -1:
    arr[i + 1] = val
    result.append(' '.join(map(str, arr)))
  return result