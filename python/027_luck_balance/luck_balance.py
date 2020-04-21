def luckBalance(k, contests):
  # sort contests first
  contests = sorted(contests, key=lambda c: (c[1], c[0]), reverse=True)

  luck = 0
  i = 0
  while i < k:
    luck += contests[i][0]
    i += 1
  while contests[i][1] == 1 and i < len(contests):
    luck -= contests[i][0]
    i += 1
  while i < len(contests):
    luck += contests[i][0]
    i += 1

  return luck


print(luckBalance(3, [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]))  # 29
