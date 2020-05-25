def insertion_sort_2(n, arr):
  def swap(left, right):
    arr[left], arr[right] = arr[right], arr[left]

  result = []
  for i in range(1, len(arr)):
    j = i - 1
    while j >= 0 and arr[j + 1] < arr[j]:
      swap(j, j + 1)
      j -= 1
    result.append(' '.join(map(str, arr)))
  return result