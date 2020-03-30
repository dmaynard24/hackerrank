def minimum_swaps(arr):
  def swap(left, right):
    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp

  swap_count = 0
  i = 0
  while i < len(arr):
    if arr[i] != i + 1:
      swap(i, arr[i] - 1)
      swap_count += 1
      i -= 1
    i += 1

  return swap_count
