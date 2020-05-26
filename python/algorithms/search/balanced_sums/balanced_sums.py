def balanced_sums(arr):
  if len(arr) == 1:
    return 'YES'
  l = len(arr) - 2
  r = len(arr)
  sum_l = sum(arr) - arr[-1]
  sum_r = 0
  while l >= -1 and sum_l >= sum_r:
    if sum_l == sum_r:
      return 'YES'
    sum_l -= arr[l]
    l -= 1
    r -= 1
    sum_r += arr[r]
  return 'NO'