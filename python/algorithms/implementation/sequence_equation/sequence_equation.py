def sequence_equation(p):
  inverse = [None] * (len(p) + 1)
  for i, num in enumerate(p):
    inverse[num] = i + 1
  return [inverse[inverse[x]] for x in range(1, len(p) + 1)]
