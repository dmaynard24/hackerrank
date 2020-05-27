def grid_challenge(grid):
  sorted_rows = [sorted(list(row)) for row in grid]
  for i in range(1, len(sorted_rows)):
    for j in range(len(sorted_rows[i])):
      if sorted_rows[i - 1][j] > sorted_rows[i][j]:
        return 'NO'
  return 'YES'