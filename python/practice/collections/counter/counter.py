from collections import Counter


def counter(sizes, size_prices):
  sizes_dict = Counter(sizes)
  money = 0
  for sp in size_prices:
    size, price = sp
    if size in sizes_dict and sizes_dict[size] > 0:
      money += price
      sizes_dict[size] -= 1
  return money
