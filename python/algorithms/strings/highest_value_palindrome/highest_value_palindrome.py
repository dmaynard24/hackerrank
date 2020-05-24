def highest_value_palindrome(s, n, k):
  arr = list(s)

  i = 0
  j = len(arr) - 1
  count = 0
  changed_indices = {}
  while i < j:
    if arr[i] != arr[j]:
      count += 1
      if count > k:
        return '-1'
      if arr[i] < arr[j]:
        arr[i] = arr[j]
      else:
        arr[j] = arr[i]
      changed_indices[i] = 1
    i += 1
    j -= 1

  if count == k:
    return ''.join(arr)
  elif count < k:
    remaining = k - count
    if remaining == 1 and len(arr) % 2 == 1:
      arr[(len(arr) // 2)] = '9'
    else:
      for i, char in enumerate(arr):
        if char != '9':
          arr[i] = '9'
          arr[len(arr) - (i + 1)] = '9'
          if i in changed_indices:
            remaining -= 1
          else:
            remaining -= 2
          if remaining <= 0:
            break
      return ''.join(arr)
    return ''.join(arr)
