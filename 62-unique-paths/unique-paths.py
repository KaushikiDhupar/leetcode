class Solution:
    def countways(self,i,j,dp):
        # Base case: If we reach the top-left corner (i=0, j=0), there is one way to reach there.
        if i==0 and j==0:
            return 1

        if i<0 or j<0: # If either i or j goes out of bounds (negative), there is no way to reach that cell.
            return 0

        # If we have already calculated the number of ways for this cell, return it from the dp array.
        if dp[i][j]!=-1:
            return dp[i][j]

        # Recursive calls to count the number of ways to reach the current cell.
        up=self.countways(i-1,j,dp) #moving up one row
        left=self.countways(i,j-1,dp) #moving left
        dp[i][j]=left+up
        return dp[i][j]

    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[-1 for _ in range(n)] for _ in range(m)]
        return self.countways(m-1,n-1,dp)
        