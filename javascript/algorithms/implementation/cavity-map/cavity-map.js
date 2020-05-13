function cavityMap(grid) {
  for (let i = 1; i < grid.length - 1; i++) {
    for (let j = 1; j < grid[i].length - 1; j++) {
      if (grid[i - 1][j] === `X`) {
        continue;
      }
      if (grid[i][j - 1] < grid[i][j] && grid[i][j + 1] < grid[i][j] && grid[i - 1][j] < grid[i][j] && grid[i + 1][j] < grid[i][j]) {
        grid[i] = `${grid[i].substring(0, j)}X${grid[i].substring(j + 1)}`;
      }
    }
  }
  return grid;
}

module.exports = { cavityMap };
