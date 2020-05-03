def reverse(num):
  r = 0
  while num > 0:
    r *= 10
    r += num % 10
    num //= 10
  return r


def beautiful_days(i, j, k):
  count = 0
  for num in range(i, j + 1):
    if abs(num - reverse(num)) % k == 0:
      count += 1
  return count