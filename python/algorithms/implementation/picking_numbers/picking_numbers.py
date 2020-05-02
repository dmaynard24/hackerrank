def picking_numbers(a):
  max_length = 0
  a.sort()
  i = 0
  while i < len(a):
    num = a[i]
    length = 1
    j = i + 1
    while j < len(a) and a[j] == num:
      length += 1
      j += 1
    next_i = j
    while j < len(a) and a[j] == num + 1:
      length += 1
      j += 1
    max_length = max(max_length, length)
    i = next_i
  return max_length