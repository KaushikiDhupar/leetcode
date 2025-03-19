class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        dp=[-1]*n
        dp[0]=nums[0]
        for i in range(1,n):
            rob=nums[i]
            if(i>1):
                rob+=dp[i-2]
            notrob=0+dp[i-1]
            dp[i]=max(rob,notrob)
        return dp[n-1]

        