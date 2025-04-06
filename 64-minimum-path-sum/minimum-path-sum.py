class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        dp=[[-1 for _ in range(cols)] for j in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if i==0 and j==0:
                    dp[i][j]=grid[i][j]
                else:
                    up = grid[i][j] + (dp[i-1][j] if i > 0 else float('inf'))
                    left = grid[i][j] + (dp[i][j-1] if j > 0 else float('inf'))
                    dp[i][j]=min(up,left)
        return dp[rows-1][cols-1]
        