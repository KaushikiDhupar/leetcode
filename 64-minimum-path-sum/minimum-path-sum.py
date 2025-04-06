class Solution:
    def solve(self,dp,i,j,grid):
        if i==0 and j==0:
            return grid[0][0]
        if i<0 or j<0:
            return float('inf')
        if dp[i][j]!=-1:
            return dp[i][j]
        up=grid[i][j]+self.solve(dp,i-1,j,grid)
        left=grid[i][j]+self.solve(dp,i,j-1,grid)
        dp[i][j]=min(up,left)
        return dp[i][j]


        

    def minPathSum(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        dp=[[-1 for _ in range(cols)] for _ in range(rows)]
        return self.solve(dp,rows-1,cols-1,grid)


        
        

        