class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows,cols=len(obstacleGrid),len(obstacleGrid[0])
        dp=[[-1 for _ in range(cols)] for _ in range(rows)]
        if obstacleGrid[0][0] == 1:
            return 0
        dp[0][0] = 1

        for i in range(rows):
            for j in range(cols):
                if obstacleGrid[i][j]==1:
                    dp[i][j]=0
                    continue
                if i==0 and j==0:
                    continue #already initialized
              
                up=0
                left=0
                
                if i>0:
                    up=dp[i-1][j]
                if j>0:
                    left=dp[i][j-1]
                dp[i][j]=up+left

        return dp[rows-1][cols-1]



        