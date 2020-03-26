def equalize_array(arr):
  cached_vals = {}
  largest_count = 0
  for val in arr:
    if val in cached_vals:
      cached_vals[val] += 1
      cached_val = cached_vals[val]
      if cached_val > largest_count:
        largest_count = cached_val
    else:
      cached_vals[val] = 1
  return len(arr) - largest_count if largest_count > 0 else len(arr) - 1
