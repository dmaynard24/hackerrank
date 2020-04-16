def commonChild(s1, s2):
  longest_count = 0

  s1_chars_indices = {}
  for i, char in enumerate(list(s1)):
    s1_chars_indices[char] = s1_chars_indices.get(char, []) + [i]

  for i, char in enumerate(list(s2)):
    if char in s1_chars_indices:
      count = 1
      prev_char_index = s1_chars_indices[char][0]
      for j in range(i + 1, len(s2)):
        if s2[j] in s1_chars_indices:
          for k in s1_chars_indices[s2[j]]:
            if k > prev_char_index:
              count += 1
              prev_char_index = k
              break
      longest_count = max(longest_count, count)

  return longest_count


print(commonChild('HARRY', 'SALLY'))  # 2
print(commonChild('AA', 'BB'))  # 0
print(commonChild('SHINCHAN', 'NOHARAAA'))  # 3
print(commonChild('ABCDEF', 'FBDAMN'))  # 2
# print(
#     commonChild('WEWOUCUIDGCGTRMEZEPXZFEJWISRSBBSYXAYDFEJJDLEBVHHKS',
#                 'FDAGCXGKCTKWNECHMRXZWMLRYUCOCZHJRRJBOAJOQJZZVUYXIC'))  # 15
