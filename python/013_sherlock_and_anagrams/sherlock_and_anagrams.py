def sherlock_and_anagrams(s):
  count = 0
  for i in range(len(s)):
    for length in range(1, len(s) - i):
      first_sub = s[i:i + length]
      for j in range(i + 1, len(s) - length + 1):
        second_sub = s[j:j + length]
        if length == 1:
          if first_sub == second_sub:
            count += 1
        else:
          first_sub = list(first_sub)
          first_sub.sort()
          ''.join(first_sub)
          second_sub = list(second_sub)
          second_sub.sort()
          ''.join(second_sub)
          if first_sub == second_sub:
            count += 1
  return count