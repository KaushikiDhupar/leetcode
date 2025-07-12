class Solution:
    def kidsWithCandies(self, candies: List[int], extra: int) -> List[bool]:
        maxi=max(candies)
        res=[]
        for can in candies:
            if can+extra<maxi:
                res.append(False)
            else:
                res.append(True)
        
        return res
        