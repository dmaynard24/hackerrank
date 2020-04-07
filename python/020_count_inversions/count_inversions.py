def countInversions(arr):
  count = 0

  def swap(left, right):
    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp
    nonlocal count
    count += 1

  def merge_halves(left, middle, right):
    left_start = left
    right_start = middle + 1

    while left_start <= middle and right_start <= right:
      if arr[left_start] <= arr[right_start]:
        left_start += 1
      else:
        swap(left_start, right_start)
        print('SWAP', arr)
        right_start += 1

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
