import math


def sherlock_and_squares(a, b):
  count = 0
  sqrt = math.sqrt(b)
  s = []
  i = 1
  while i <= sqrt:
    s.append(i**2)
    i += 1
  for num in s:
    if num >= a and num <= b:
      count += 1
  return count
