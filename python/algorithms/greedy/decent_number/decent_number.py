def decent_number(n):
  if n < 3:
    return '-1'
  if n % 3 == 0:
    return '5' * n
  else:
    new_n = n
    while new_n > 0:
      if new_n % 3 == 0:
        return '5' * new_n + '3' * (n - new_n)
      new_n -= 5
    new_n = n
    while new_n > 0:
      if new_n % 5 == 0:
        return '5' * (n - new_n) + '3' * new_n
      new_n -= 3
    return '-1'