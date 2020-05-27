def beautiful_pairs(a, b):
  count = 0
  a.sort()
  b.sort()
  i = 0
  j = 0
  while i < len(a) and j < len(b):
    if a[i] == b[j]:
      count += 1
      i += 1
      j += 1
    elif a[i] < b[j]:
      i += 1
    else:
      j += 1
  if count < len(a):
    return count + 1
  elif count == len(a):
    return count - 1
  else:
    return count