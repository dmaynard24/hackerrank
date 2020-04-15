def alternatingCharacters(s):
  deletion_count = 0
  i = 1
  while i < len(s):
    if s[i] == s[i - 1]:
      deletion_count += 1
    i += 1
  return deletion_count


print(alternatingCharacters('AAAA'))  # 3
print(alternatingCharacters('BBBBB'))  # 4
print(alternatingCharacters('ABABABAB'))  # 0
print(alternatingCharacters('BABABA'))  # 0
print(alternatingCharacters('AAABBB'))  # 4
