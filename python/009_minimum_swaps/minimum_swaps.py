def minimum_swaps(arr):
  swap_count = 0

  def swap(left, right):
    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp
    nonlocal swap_count
    swap_count += 1

  unsorted_count = 0
  for i in range(len(arr)):
    if arr[i] != i + 1:
      unsorted_count += 1

  while (unsorted_count > 0):
    largest_diff = 0
    largest_diff_index = None
    for i in range(len(arr)):
      diff = abs(arr[i] - (i + 1))
      if diff != 0:
        if diff > largest_diff:
          largest_diff = diff
          largest_diff_index = i

    right = arr[largest_diff_index] - 1
    if largest_diff_index + 1 == arr[right]:
      unsorted_count -= 2
    else:
      unsorted_count -= 1
    swap(largest_diff_index, right)

  return swap_count


print(minimum_swaps([2, 3, 4, 1, 5]))  # 3
# print(minimum_swaps([1, 3, 5, 2, 4, 6, 7]))  # 3
