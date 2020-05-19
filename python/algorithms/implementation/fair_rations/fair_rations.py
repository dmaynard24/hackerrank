def fair_rations(b):
  if sum(b) % 2 == 1:
    return 'NO'

  count = 0
  for i in range(len(b)):
    if b[i] % 2 == 1:
      b[i] += 1
      if i == 0:
        b[i + 1] += 1
      elif i == len(b) - 1:
        b[i - 1] += 1
      else:
        if b[i - 1] % 2 == 1:
          b[i - 1] += 1
        else:
          b[i + 1] += 1
      count += 2
  return count