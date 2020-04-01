def maximumToys(prices, k):
  prices.sort()

  count = 0
  while k - prices[count] >= 0:
    k -= prices[count]
    count += 1

  return count


print(maximumToys([1, 12, 5, 111, 200, 1000, 10], 50))