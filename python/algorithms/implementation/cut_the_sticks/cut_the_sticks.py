def cut_the_sticks(arr):
  l = len(arr)
  remaining = [l]
  arr.sort()
  length_cut = arr[0]
  for i in range(1, l):
    if arr[i] != length_cut:
      length_cut = arr[i]
      remaining.append(l - i)
  return remaining