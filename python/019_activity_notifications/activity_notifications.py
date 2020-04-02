def activityNotifications(expenditure, d):
  def insert_sorted(arr, val, left, right):
    if len(arr) == 0:
      arr.append(val)
    else:
      if left < right - 1:
        middle = (left + right) // 2
        if arr[middle] <= val:
          insert_sorted(arr, val, middle, right)
        else:
          insert_sorted(arr, val, left, middle)
      else:
        if arr[right] < val:
          arr.insert(right + 1, val)
        else:
          arr.insert(right, val)

  count = 0

  is_even_d = d % 2 == 0
  prev_sorted = []
  for i in range(0, len(expenditure)):
    val = expenditure[i]
    if i >= d:
      if is_even_d:
        median = (prev_sorted[d // 2 - 1] + prev_sorted[d // 2]) / 2
      else:
        median = prev_sorted[d // 2]
      if val >= 2 * median:
        count += 1
      # print(prev_sorted, median, val)
      prev_sorted.pop(0)
    insert_sorted(prev_sorted, val, 0, len(prev_sorted) - 1)

  return count


print(activityNotifications([2, 3, 4, 2, 3, 6, 8, 4, 5], 5))  # 2
print(activityNotifications([1, 2, 3, 4, 4], 4))  # 0