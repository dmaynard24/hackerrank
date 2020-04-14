def countInversions(arr):
  count = 0

  def merge_halves(left, middle, right):
    temp = []
    left_start = left
    right_start = middle + 1
    size = right - left + 1

    while left_start <= middle and right_start <= right:
      if arr[left_start] <= arr[right_start]:
        temp.append(arr[left_start])
        left_start += 1
      else:
        temp.append(arr[right_start])
        right_start += 1
        nonlocal count
        count += middle - left + 1 - left_start

    if left_start <= middle:
      temp.extend(arr[left_start:middle + 1])
    else:
      temp.extend(arr[right_start:right + 1])

    arr[left:left + size] = temp
    print(arr, count)

  def mergesort(left, right):
    if left < right:
      middle = (left + right) // 2
      mergesort(left, middle)
      mergesort(middle + 1, right)
      merge_halves(left, middle, right)

  mergesort(0, len(arr) - 1)

  return count


print(countInversions([1, 1, 1, 2, 2]))  # 0
print(countInversions([2, 1, 3, 1, 2]))  # 4
print(countInversions([7, 5, 3, 1]))  # 6
print(countInversions([3, 2, 1]))  # 3
