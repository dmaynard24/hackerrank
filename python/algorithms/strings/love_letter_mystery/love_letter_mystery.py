def love_letter_mystery(s):
  l = 0
  r = len(s) - 1
  count = 0
  while l < r:
    if s[l] != s[r]:
      ord_l = ord(s[l])
      ord_r = ord(s[r])
      if ord_l < ord_r:
        count += ord_r - ord_l
      else:
        count += ord_l - ord_r
    l += 1
    r -= 1
  return count