class Solution:
  def findMaxFish(self, grid: list[list[int]]) -> int:
    def dfs(i: int, j: int) -> int:
      if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]):
        return 0
      if grid[i][j] == 0:
        return 0
      caughtFish = grid[i][j]
      grid[i][j] = 0  # Mark 0 as visited
      return (caughtFish +
              dfs(i + 1, j) + dfs(i - 1, j) +
              dfs(i, j + 1) + dfs(i, j - 1))

    return max(dfs(i, j)
               for i in range(len(grid))
               for j in range(len(grid[0])))