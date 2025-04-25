class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n=len(nums)
        maxlen=0
        l=0
        r=0
        length=0
        zeros=0
        while r<n:

            if nums[r]==0:
                zeros=zeros+1
            while zeros>k:
                if nums[l]==0:
                    zeros-=1
                l+=1
            if zeros<=k:
                length=r-l+1
                maxlen=max(maxlen,length)
            r+=1
        return maxlen



        