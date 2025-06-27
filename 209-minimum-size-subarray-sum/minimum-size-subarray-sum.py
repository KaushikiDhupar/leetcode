class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        r,l,sumi=0,0,0
        n=len(nums)
        mini = float('inf')
        while r<n:
            sumi+=nums[r]

            while sumi>=target:
                mini=min(mini,r-l+1)
                sumi-=nums[l]
                l=l+1
            r+=1

        return 0 if mini ==float('inf') else mini
        