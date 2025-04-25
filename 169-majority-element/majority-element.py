class Solution(object):
    def majorityElement(self, nums):
        dict1={}
        for i in nums:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
        a=max(dict1.values())
        for k,v in dict1.items():
            if v==a:
                return k