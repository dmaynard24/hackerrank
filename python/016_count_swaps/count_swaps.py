def count_swaps(a):
  def swap(left, right):
    a[left], a[right] = a[right], a[left]

  def bubblesort():
    count = 0
    for _ in range(len(a)):
      for j in range(len(a) - 1):
        if a[j] > a[j + 1]:
          # swap elements if they are in decreasing order
          swap(j, j + 1)
          count += 1
    return count

  count = bubblesort()

  print(str.format('Array is sorted in {} swaps.', count))
  print(str.format('First Element: {}', a[0]))
  print(str.format('Last Element: {}', a[-1]))
  return count


count_swaps([6, 4, 1])
count_swaps([1, 2, 3])
count_swaps([3, 2, 1])
