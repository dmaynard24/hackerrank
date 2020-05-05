def sequence_equation(p):
  result = []
  inverse = [None] * (len(p) + 1)
  for i, num in enumerate(p):
    inverse[num] = i + 1
  for x in range(1, len(p) + 1):
    result.append(inverse[inverse[x]])
  return result
