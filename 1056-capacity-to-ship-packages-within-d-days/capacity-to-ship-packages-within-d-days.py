class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def func(mid,weights):
            singleday=0
            load=0
            for weight in weights:
                if load+weight>mid:
                    singleday+=1
                    load=0
                load+=weight
            return singleday
        low,high=max(weights),sum(weights)
        while low<=high:
            mid=(high+low)//2
            NoOfDays=func(mid,weights)
            if NoOfDays<days:
                high=mid-1
            else:
                low=mid+1
        return low
                

        