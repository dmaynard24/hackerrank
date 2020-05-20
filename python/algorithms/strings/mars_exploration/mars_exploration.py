def mars_exploration(s):
  count = 0
  expected = 'SOS'
  for i in range(len(s)):
    if s[i] != expected[i % len(expected)]:
      count += 1
  return count