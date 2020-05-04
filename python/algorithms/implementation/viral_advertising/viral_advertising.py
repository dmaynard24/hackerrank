def viral_advertising(n):
  count = 0
  shared = 5
  for i in range(n):
    likes = shared // 2
    shared = likes * 3
    count += likes
  return count