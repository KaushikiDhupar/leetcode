class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #initialize a dp array
        dp=[[0 for _ in range(n)] for _ in range(m)]
        dp[0][0]=1
        for i in range(m):
            for j in range(n):
                 # Base condition: If we are at the top-left corner, there is one way to reach it.
                if i == 0 and j == 0:
                    dp[i][j] = 1
                    continue
                
                # Initialize variables to store the number of ways from above and from the left.
                up = 0
                left = 0
                if i>0:
                    up=dp[i-1][j]
                if j>0:
                    left=dp[i][j-1]
                dp[i][j]=up+left
        return dp[m-1][n-1]
        