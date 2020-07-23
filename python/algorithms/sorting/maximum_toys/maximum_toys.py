def maximum_toys(prices, k):
  prices.sort()

  count = 0
  while k - prices[count] >= 0:
    k -= prices[count]
    count += 1

  return count
