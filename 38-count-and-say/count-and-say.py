class Solution:
    def countAndSay(self, n: int) -> str:
        return reduce(lambda s,_:''.join(str(len([*g]))+c for c,g in groupby(s)),range(n-1),'1')

        