class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        flag=True
        for i in range(n):
            if nums[i]==0:
                flag=False
                break

        maxlen,l,r,k=0,0,0,1
        while r<n:
            if nums[r] == 0:
                k -= 1
            while k<0:
                if nums[l]==0:
                    k+=1
                l+=1
                
            maxlen=max(maxlen,r-l)
            r+=1

        if flag:
            return n-1
        else:
            return maxlen