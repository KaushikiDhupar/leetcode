class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d={}
        for num in nums:
            if num in d:
                d[num]+=1
            else:
                d[num]=1
        for key,value in d.items():
            if value>1:
                return key
        
        