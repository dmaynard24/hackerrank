def icecream_parlor(m, arr):
  prices = {}
  for i in range(len(arr)):
    remaining = m - arr[i]
    if remaining in prices:
      return sorted([i + 1, prices[remaining] + 1])
    prices[arr[i]] = i