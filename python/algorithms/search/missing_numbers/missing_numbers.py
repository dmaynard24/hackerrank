def missing_numbers(arr, brr):
  arr_counts = {}
  for num in arr:
    arr_counts[num] = arr_counts.get(num, 0) + 1

  missing_nums = set()
  for num in brr:
    if num not in arr_counts:
      missing_nums.add(num)
    else:
      arr_counts[num] -= 1
      if arr_counts[num] < 0:
        missing_nums.add(num)

  return sorted(missing_nums)