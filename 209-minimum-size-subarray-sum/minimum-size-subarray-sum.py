class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums)<target:
            return 0
        i,j,sumi,n=0,0,0,len(nums)
        minl=len(nums)
        while j<n:
            sumi+=nums[j]

            while sumi>=target:
                minl=min(minl,j-i+1)
                sumi-=nums[i]
                i+=1
            j+=1


        return minl
        