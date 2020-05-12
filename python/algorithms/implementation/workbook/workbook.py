import math


def workbook(n, k, arr):
  count = 0
  page = 1
  for num in arr:
    if num < page:
      page += math.ceil(num / k)
      continue
    for i in range(1, num + 1):
      if i == page:
        count += 1
      if i % k == 0:
        page += 1
    if num % k != 0:
      page += 1
  return count