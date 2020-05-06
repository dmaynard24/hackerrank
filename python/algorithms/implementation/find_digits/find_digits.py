def find_digits(n):
  count = 0
  original_n = n
  while n > 0:
    digit = n % 10
    n //= 10
    if digit > 0 and original_n % digit == 0:
      count += 1
  return count