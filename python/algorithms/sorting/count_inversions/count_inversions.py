def count_inversions(arr):
  def merge_halves(left, middle, right):
    count = 0
    temp = []
    left_start = left
    right_start = middle + 1
    size = right - left + 1

    while left_start <= middle and right_start <= right:
      if arr[left_start] > arr[right_start]:
        temp.append(arr[right_start])
        count += middle - left_start + 1  # tricky
        right_start += 1
      else:
        temp.append(arr[left_start])
        left_start += 1

    if left_start <= middle:
      temp.extend(arr[left_start:middle + 1])
    else:
      temp.extend(arr[right_start:right + 1])

    arr[left:left + size] = temp

    return count

  def mergesort(left, right):
    count = 0

    if left < right:
      middle = (left + right) // 2
      count += mergesort(left, middle)
      count += mergesort(middle + 1, right)
      count += merge_halves(left, middle, right)

    return count

  return mergesort(0, len(arr) - 1)
