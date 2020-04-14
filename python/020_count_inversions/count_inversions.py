def countInversions(arr):
  count = 0

  def merge_halves(left, middle, right):
    left_start = left
    right_start = middle + 1

    while left_start <= middle and right_start <= right:
      if arr[left_start] <= arr[right_start]:
        left_start += 1
      else:
        right_start += 1

    # create temp and reconstruct here, counting inversions beforehand

  def mergesort(left, right):
    if left < right:
      middle = (left + right) // 2
      mergesort(left, middle)
      mergesort(middle + 1, right)
      merge_halves(left, middle, right)

  mergesort(0, len(arr) - 1)

  return count


# print(countInversions([1, 1, 1, 2, 2]))  # 0
print(countInversions([2, 1, 3, 1, 2]))  # 4
# print(countInversions([7, 5, 3, 1])) # 6