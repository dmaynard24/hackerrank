import math


def kaprekar_numbers(p, q):
  kaprekars = []
  for i in range(p, q + 1):
    sq = i**2
    digit_count = math.floor(math.log10(i)) + 1
    r = sq % (10**digit_count)
    sq //= (10**digit_count)
    if sq + r == i:
      kaprekars.append(i)
  if len(kaprekars) == 0:
    return 'INVALID RANGE'
  return kaprekars