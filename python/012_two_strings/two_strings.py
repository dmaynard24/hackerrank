def two_strings(s1, s2):
  s1_chars = {char: True for char in s1}
  s2_chars = {char: True for char in s2}
  if len(s1_chars) < len(s2_chars):
    for char in s1_chars:
      if char in s2_chars:
        return 'YES'
  else:
    for char in s2_chars:
      if char in s1_chars:
        return 'YES'
  return 'NO'