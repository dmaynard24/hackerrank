def full_counting_sort(arr):
  sorted_arr = [[] for i in range(100)]
  for i in range(len(arr)):
    x, s = arr[i]
    sorted_arr[int(x)].append('-' if i < len(arr) // 2 else s)
  return ' '.join([' '.join(a) for a in sorted_arr]).strip()
