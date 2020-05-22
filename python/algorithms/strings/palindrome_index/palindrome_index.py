def palindrome_index(s):
  def is_array_palindrome(arr):
    l = 0
    r = len(arr) - 1
    while l < r:
      if arr[l] != arr[r]:
        return False
      l += 1
      r -= 1
    return True

  l = 0
  r = len(s) - 1
  skip_i = -1
  while l < r:
    if s[l] != s[r]:
      if is_array_palindrome(s[:l] + s[l + 1:]):
        return l
      elif is_array_palindrome(s[:r] + s[r + 1:]):
        return r
      else:
        return -1
    else:
      l += 1
      r -= 1
  return skip_i