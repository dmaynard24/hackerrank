def get_money_spent(keyboards, drives, b):
  max_sum = -1

  # sort descending for easy flow control
  keyboards.sort(reverse=True)
  drives.sort(reverse=True)

  for keyboard in keyboards:
    if keyboard >= b:
      continue
    for drive in drives:
      pair_sum = keyboard + drive
      if pair_sum == b:
        return pair_sum
      elif pair_sum < b:
        max_sum = max(max_sum, pair_sum)
        break

  return max_sum