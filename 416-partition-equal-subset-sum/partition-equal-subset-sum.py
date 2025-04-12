from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        n = len(nums)

        if total % 2 != 0:
            return False

        target = total // 2
        dp = [[False for _ in range(target + 1)] for _ in range(n)]

        # Base Case: Sum 0 is always possible
        for i in range(n):
            dp[i][0] = True

        # Base Case for the first element
        if nums[0] <= target:
            dp[0][nums[0]] = True

        # Fill the dp table
        for i in range(1, n):
            for j in range(1, target + 1):
                nottake = dp[i - 1][j]
                take = False
                if nums[i] <= j:
                    take = dp[i - 1][j - nums[i]]
                dp[i][j] = take or nottake

        return dp[n - 1][target]
