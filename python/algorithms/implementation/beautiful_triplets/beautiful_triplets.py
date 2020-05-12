def beautiful_triplets(d, arr):
  count = 0
  nums = {num: 1 for num in arr}
  for num in arr:
    if num + d in nums and num + d * 2 in nums:
      count += 1
  return count