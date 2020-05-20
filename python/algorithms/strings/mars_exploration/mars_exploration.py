def mars_exploration(s):
  count = 0
  for i in range(len(s)):
    if (i + 1) % 3 == 1 or (i + 1) % 3 == 0:
      if s[i] != 'S':
        count += 1
    else:
      if s[i] != 'O':
        count += 1
  return count