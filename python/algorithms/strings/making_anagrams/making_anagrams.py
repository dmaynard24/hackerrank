def making_anagrams(s1, s2):
  s1_chars = {}
  s2_chars = {}
  for char in s1:
    s1_chars[char] = s1_chars.get(char, 0) + 1
  for char in s2:
    s2_chars[char] = s2_chars.get(char, 0) + 1
  count = 0
  for char in s1_chars:
    if char in s2_chars:
      count += abs(s1_chars[char] - s2_chars[char])
    else:
      count += s1_chars[char]
  for char in s2_chars:
    if char not in s1_chars:
      count += s2_chars[char]
  return count