def substrCount(n, s):
  count = n  # each individual char

  for i, char in enumerate(s):
    different_char_index = None
    for j in range(i + 1, n):
      if char == s[j]:
        if different_char_index is None:
          count += 1
        elif j - different_char_index == different_char_index - i:
          count += 1
          break
      else:
        if different_char_index is None:
          different_char_index = j
        else:
          break

  return count


print(substrCount(5, 'asasd'))  # 7
print(substrCount(7, 'abcbaba'))  # 10
print(substrCount(4, 'aaaa'))  # 10
