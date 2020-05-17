import math


def absolute_permutation(n, k):
  if k == 0:
    return list(range(1, n + 1))
  if n % 2 == 0 and k <= n / 2:
    if k == n / 2:
      return list(range(n // 2 + 1, n + 1)) + list(range(1, n // 2 + 1))
    if (n % k == 0 and n / k % 2 == 0) or k == 1:
      result = []
      plus = True
      for i in range(n):
        if i > 0 and i % k == 0:
          plus = not plus
        if plus:
          result.append((i + k) + 1)
        else:
          result.append((i - k) + 1)
      return result
  return [-1]
