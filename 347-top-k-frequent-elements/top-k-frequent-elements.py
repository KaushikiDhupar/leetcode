import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        res=[]
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        max_heap=[(-count,num) for num,count in d.items()] 
        heapq.heapify(max_heap)
        for _ in range(k):

            res.append(heapq.heappop(max_heap)[1])
        return res
        
        