from typing import List

class Solution:
    def solve(self, triangle, i, j, dp):
        if i == len(triangle) - 1:
            return triangle[i][j]

        if j >= len(triangle[i]):
            return float('inf')

        if dp[i][j] != -1:
            return dp[i][j]

        same = self.solve(triangle, i + 1, j, dp)
        plusone = self.solve(triangle, i + 1, j + 1, dp)
        dp[i][j] = triangle[i][j] + min(same, plusone)

        return dp[i][j]

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[-1 for _ in range(len(triangle[i]))] for i in range(len(triangle))]
        return self.solve(triangle, 0, 0, dp)
