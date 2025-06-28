class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d={}
        for num in arr:
            if num in d:
                d[num]+=1
            else:
                d[num]=1
        seti=set()
        for value in d.values():
            if value in seti:
                return False
            seti.add(value)
        return True