import math


def print_integer(n):
  result = 0
  i = 1
  while i <= n:
    result *= 10**(math.floor(math.log10(i)) + 1)
    result += i
    i += 1
  return result