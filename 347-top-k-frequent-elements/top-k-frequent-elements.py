class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        res=[]
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        sorted_dict = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        for key in sorted_dict:
            if k == 0:
                break
            res.append(key)
            k -= 1


        return res
        