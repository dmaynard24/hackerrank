def anagram(s):
  if len(s) % 2 == 1:
    return -1
  fh_chars = {}
  sh_chars = {}
  for i in range(len(s) // 2):
    fh_chars[s[i]] = fh_chars.get(s[i], 0) + 1
    sh_chars[s[len(s) - (i + 1)]] = sh_chars.get(s[len(s) - (i + 1)], 0) + 1
  count = 0
  for char in fh_chars:
    if char in sh_chars:
      count += max(0, fh_chars[char] - sh_chars[char])
    else:
      count += fh_chars[char]
  return count