def luck_balance(k, contests):
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
