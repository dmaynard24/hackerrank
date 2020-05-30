def get_digit_sum(num):
  digit_sum = 0
  while num > 0:
    digit_sum += num % 10
    num //= 10
  return digit_sum


def get_super_digit(num):
  if num < 10:
    return num
  return get_super_digit(get_digit_sum(num))


def super_digit(n, k):
  num_sum = sum([int(d) for d in n]) * k
  return get_super_digit(num_sum)
