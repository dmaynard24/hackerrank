def cavity_map(grid):
  for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[i]) - 1):
      if grid[i][j] == 'X':
        continue
      if (grid[i][j - 1] < grid[i][j] and grid[i][j + 1] < grid[i][j]
          and grid[i - 1][j] < grid[i][j] and grid[i + 1][j] < grid[i][j]):
        grid[i] = grid[i][:j] + 'X' + grid[i][j + 1:]
  return grid