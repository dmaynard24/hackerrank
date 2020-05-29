def power_sum(x, n):
  base_limit = round(x**(1 / n))  # nth root of x

  def get_sum_count(base, running_sum):
    if running_sum == x:
      return 1
    if running_sum > x:
      return 0

    count = 0
    for b in range(base, base_limit + 1):
      power = b**n
      running_sum += power
      count += get_sum_count(b + 1, running_sum)
      running_sum -= power
    return count

  return get_sum_count(1, 0)