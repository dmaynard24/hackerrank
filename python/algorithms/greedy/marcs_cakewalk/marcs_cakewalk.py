def marcs_cakewalk(calorie):
  calorie.sort(reverse=True)

  miles = 0
  for i, cal in enumerate(calorie):
    miles += 2**i * cal

  return miles
