class Solution:
    def __init__(self):
        self.dp={}
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''n=len(cost)

        def solve(i):

            if i>=n:
                return 0
            if n in self.dp:
                return self.dp[n]
            a=cost[i]+solve(i+1)
            b=cost[i]+solve(i+2)
            self.dp[i]=min(a,b)
            return self.dp[i]

        return min(solve(0),solve(1))'''
        cost.append(0)
        n=len(cost)

        for i in range(n-3,-1,-1):
            cost[i]+=min(cost[i+1],cost[i+2])
        return min(cost[0],cost[1])
            


            





        
