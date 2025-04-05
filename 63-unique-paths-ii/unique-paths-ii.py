class Solution:
    def solve(self,dp,i,j,obstacleGrid):
        if i>=0 and j>=0 and obstacleGrid[i][j]==1:
            return 0
        if i<0 or j<0:
            return 0
        if i==0 and j==0:
            return 1
        if dp[i][j]!=-1:
            return dp[i][j]
        up=self.solve(dp,i-1,j,obstacleGrid)
        left=self.solve(dp,i,j-1,obstacleGrid)
        dp[i][j]=up+left
        return dp[i][j]
    
    
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp=[[-1 for j in range(n)] for i in range(m)]
        return self.solve(dp,m-1,n-1,obstacleGrid)
        
        

        