def countSwaps(a):
  count = 0

  def swap(left, right):
    temp = a[left]
    a[left] = a[right]
    a[right] = temp
    nonlocal count
    count += 1

  def bubblesort():
    for _ in range(len(a)):
      for j in range(len(a) - 1):
        if a[j] > a[j + 1]:
          # swap elements if they are in decreasing order
          swap(j, j + 1)

  bubblesort()

  print(str.format('Array is sorted in {} swaps.', count))
  print(str.format('First Element: {}', a[0]))
  print(str.format('Last Element: {}', a[-1]))
  return count


countSwaps([6, 4, 1])
countSwaps([1, 2, 3])
countSwaps([3, 2, 1])
