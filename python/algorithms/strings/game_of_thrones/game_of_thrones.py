def game_of_thrones(s):
  if len(s) == 1:
    return 'YES'
  s_chars = {}
  for char in s:
    s_chars[char] = s_chars.get(char, 0) + 1
  char_counts = list(set([v for v in s_chars.values()]))
  if len(s) % 2 == 0:
    for char_count in char_counts:
      if char_count % 2 != 0:
        return 'NO'
    return 'YES'
  else:
    if len(char_counts) != 2:
      return 'NO'
    elif char_counts[0] == 1 or char_counts[1] == 1 or abs(
        char_counts[0] - char_counts[1]) == 1:
      return 'YES'
    return 'NO'