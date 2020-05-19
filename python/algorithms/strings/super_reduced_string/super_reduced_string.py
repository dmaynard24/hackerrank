def super_reduced_string(s):
  arr = list(s)
  i = 0
  while len(arr) > 0 and i < len(arr) - 1:
    if arr[i] == arr[i + 1]:
      del arr[i]
      del arr[i]
      i = 0
    else:
      i += 1
  return 'Empty String' if len(arr) == 0 else ''.join(arr)