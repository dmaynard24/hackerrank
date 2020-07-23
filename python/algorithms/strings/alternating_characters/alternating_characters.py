def alternating_characters(s):
  deletion_count = 0
  i = 1
  while i < len(s):
    if s[i] == s[i - 1]:
      deletion_count += 1
    i += 1
  return deletion_count
