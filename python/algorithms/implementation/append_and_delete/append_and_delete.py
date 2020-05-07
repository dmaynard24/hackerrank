def append_and_delete(s, t, k):
  # early return, k is large enough to completely delete one of the words and replace it by appending all chars of the other
  if k >= len(s) + len(t):
    return 'Yes'

  # l is the length of the longest shared prefix
  l = 0
  while l < len(s) and l < len(t) and s[l] == t[l]:
    l += 1
  diff = (len(s) - l) + (len(t) - l)
  if k == diff:
    return 'Yes'
  elif k > diff and k % 2 == diff % 2:
    return 'Yes'
  else:
    return 'No'