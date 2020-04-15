def substrCount(n, s):
  count = n  # each individual char

  def is_substr_special_palindrome(left, right):
    same_char = s[left]
    while left < right:
      if s[left] != s[right] or s[left] != same_char or s[right] != same_char:
        return False
      left += 1
      right -= 1

    return True

  for i in range(0, n):
    for j in range(1, n - i):
      if is_substr_special_palindrome(i, i + j):
        count += 1

  return count


print(substrCount(5, 'asasd'))  # 7
print(substrCount(7, 'abcbaba'))  # 10
print(substrCount(4, 'aaaa'))  # 10
