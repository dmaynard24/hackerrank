def sequence_equation(p):
  result = []
  for i in range(1, len(p) + 1):
    first_index = p.index(i)
    second_index = p.index(first_index + 1)
    result.append(second_index + 1)
  return result