import re


def minimum_number(n, password):
  missing = 0
  if re.search(r'[0-9]', password) is None:
    missing += 1
  if re.search(r'[a-z]', password) is None:
    missing += 1
  if re.search(r'[A-Z]', password) is None:
    missing += 1
  if re.search(r'[\!\@\#\$\%\^\&\*\(\)\-\+]', password) is None:
    missing += 1
  return max(missing, 6 - n)