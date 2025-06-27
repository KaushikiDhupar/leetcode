class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxlen=0
        n=len(nums)
        r=l=0
        while r<n:
            if nums[r]==0:
                k=k-1

            while k<0:
                if nums[l]==0:
                    k+=1
                l+=1
            maxlen=max(maxlen,r-l+1)
            r+=1
        return maxlen