def quicksort_1(arr):
  l = []
  e = [arr[0]]
  r = []
  for i in range(1, len(arr)):
    if arr[i] < arr[0]:
      l.append(arr[i])
    elif arr[i] == arr[0]:
      e.append(arr[i])
    else:
      r.append(arr[i])
  return l + e + r