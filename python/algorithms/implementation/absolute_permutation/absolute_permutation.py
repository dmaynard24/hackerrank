def absolute_permutation(n, k):
  if k == 0:
    return list(range(1, n + 1))
  if n % 2 == 0 and k <= n / 2:
    if n % k == 0 and n / k % 2 == 0:
      result = []
      is_plus = False
      for i in range(n):
        if i % k == 0:
          is_plus = not is_plus
        if is_plus:
          result.append((i + k) + 1)
        else:
          result.append((i - k) + 1)
      return result
  return [-1]