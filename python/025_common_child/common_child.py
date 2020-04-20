def commonChild(s1, s2):
  a = len(s1)
  prev = [0] * (a + 1)
  curr = [0] * (a + 1)
  for i in reversed(range(a)):
    for j in reversed(range(a)):
      if s1[i] == s2[j]:
        curr[j] = prev[j + 1] + 1
      else:
        curr[j] = max(curr[j + 1], prev[j])
    prev, curr = curr, prev
  return prev[0]


print(commonChild('HARRY', 'SALLY'))  # 2
print(commonChild('AA', 'BB'))  # 0
print(commonChild('SHINCHAN', 'NOHARAAA'))  # 3
print(commonChild('ABCDEF', 'FBDAMN'))  # 2
print(
    commonChild('WEWOUCUIDGCGTRMEZEPXZFEJWISRSBBSYXAYDFEJJDLEBVHHKS',
                'FDAGCXGKCTKWNECHMRXZWMLRYUCOCZHJRRJBOAJOQJZZVUYXIC'))  # 15
