def separate_numbers(s):
  if s[0] == '0':
    return 'NO'

  def get_first_num(start, min_length, nums):
    if start == len(s):
      return nums[0]

    for length in range(min_length, len(s) - start + 1):
      if s[start:start + 1] != '0':
        num = int(s[start:start + length])
        nums.append(num)
        if nums[-1] - nums[-2] == 1:
          return get_first_num(start + length, length, nums)
        nums.pop()

    return -1

  for length in range(1, len(s) // 2 + 1):
    num = get_first_num(length, length, [int(s[:length])])
    if num != -1:
      return 'YES ' + str(num)

  return 'NO'