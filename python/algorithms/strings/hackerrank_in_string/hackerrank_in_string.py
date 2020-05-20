def hackerrank_in_string(s):
  target = 'hackerrank'
  i = 0
  for char in s:
    if char == target[i]:
      if i == len(target) - 1:
        return 'YES'
      i += 1
  return 'NO'