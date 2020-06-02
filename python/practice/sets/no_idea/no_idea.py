def no_idea(arr, a, b):
  count = 0
  for num in arr:
    count += (num in a) - (num in b)
  return count