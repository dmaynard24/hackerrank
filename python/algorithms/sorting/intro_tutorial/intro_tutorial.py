def intro_tutorial(V, arr):
  def binary_search(left, right):
    if arr[left] == V:
      return left
    if arr[right] == V:
      return right
    middle = (left + right) // 2
    if arr[middle] == V:
      return middle
    if left <= right:
      if arr[middle] < V:
        return binary_search(middle + 1, right)
      return binary_search(left, middle)
    return -1

  return binary_search(0, len(arr) - 1)