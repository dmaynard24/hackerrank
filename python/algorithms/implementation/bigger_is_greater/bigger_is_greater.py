def bigger_is_greater(w):
  # check if already largest perm
  i = len(w) - 1
  while i > 0 and w[i - 1] >= w[i]:
    i -= 1
  if i == 0:
    return 'no answer'

  # find pivot, swap
  i -= 1
  arr = list(w)
  j = len(w) - 1
  while w[j] <= w[i]:
    j -= 1
  arr[i], arr[j] = arr[j], arr[i]

  # reverse suffix
  suff = arr[i + 1:]
  suff.reverse()
  arr[i + 1:] = suff

  return ''.join(arr)