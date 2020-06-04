def designer_door_mat(n, m):
  result = []

  row_limit = (n + 1) // 2

  for row in range(1, row_limit):
    pattern_count = (row * 2) - 1
    result.append(('.|.' * pattern_count).center(m, '-'))

  result.append('WELCOME'.center(m, '-'))

  for row in range(1, row_limit):
    pattern_count = ((row_limit - row) * 2) - 1
    result.append(('.|.' * pattern_count).center(m, '-'))

  return result