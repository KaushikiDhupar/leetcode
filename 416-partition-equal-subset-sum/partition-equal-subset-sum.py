class Solution:
    def subsetsum(self,i,target,nums,dp):
        if target==0:
            return True
        if i==0:
            return nums[0]==target
        if dp[i][target]!=-1:
            return dp[i][target]
        nottake=self.subsetsum(i-1,target,nums,dp)
        take=False
        if nums[i]<=target:
            take=self.subsetsum(i-1,target-nums[i],nums,dp)
        dp[i][target]=nottake or take
        return dp[i][target]

    def canPartition(self, nums: List[int]) -> bool:
        sum1=0
        n=len(nums)
        for j in range(n):
            sum1+=nums[j]
        if sum1%2!=0:
            return False
        else:
            target=sum1//2
            dp=[[-1 for _ in range(target+1)] for _ in range(n)]
            return self.subsetsum(n-1,target,nums,dp)
        