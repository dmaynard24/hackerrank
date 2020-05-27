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


def gridChallenge(grid):
  sorted_rows = [sorted(list(row)) for row in grid]
  for i in range(1, len(sorted_rows)):
    for j in range(len(sorted_rows[i])):
      if sorted_rows[i - 1][j] > sorted_rows[i][j]:
        return 'NO'
  return 'YES'