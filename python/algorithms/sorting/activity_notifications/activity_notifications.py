def activity_notifications(expenditure, d):
  count = 0
  count_arr = [0] * 201

  for i in range(0, d):
    count_arr[expenditure[i]] += 1

  for i in range(d, len(expenditure)):
    if expenditure[i] >= get_median_val(count_arr, d) * 2:
      count += 1
    count_arr[expenditure[i - d]] -= 1
    count_arr[expenditure[i]] += 1

  return count


def get_median_val(count_arr, d):
  is_even_len = d % 2 == 0
  total_count = 0

  for i, count in enumerate(count_arr):
    total_count += count
    if is_even_len:
      if total_count == d // 2:
        for j in range(i + 1, len(count_arr)):
          if count_arr[j] > 0:
            return (i + j) / 2
      elif total_count > d // 2:
        return i
    else:
      if total_count >= d // 2 + 1:
        return i