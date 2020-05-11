import math


def encryption(s):
  s = s.replace(' ', '')
  sqrt = math.sqrt(len(s))
  col_count = math.ceil(sqrt)
  row_count = col_count
  encrypted = ''
  for col in range(col_count):
    for row in range(row_count):
      i = row * col_count + col
      if i < len(s):
        encrypted += s[i]
    if col == col_count - 1:
      break
    encrypted += ' '
  return encrypted