def weighted_uniform_strings(s, queries):
  weights = {}
  i = 0
  while i < len(s):
    char_weight = ord(s[i]) - 96
    weight = char_weight
    weights[weight] = 1
    j = 1
    while i + j < len(s) and s[i] == s[i + j]:
      weight += char_weight
      weights[weight] = 1
      j += 1
    i += j
  return ['Yes' if q in weights else 'No' for q in queries]