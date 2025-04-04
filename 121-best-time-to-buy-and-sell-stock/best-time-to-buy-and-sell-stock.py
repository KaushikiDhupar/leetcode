class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=float('inf') #initialize with mac value
        n=len(prices)
        profit=0
        for i in range(n):
            if mini>prices[i]:
                mini=prices[i]
            elif ((prices[i]-mini)>profit):
                profit=prices[i]-mini
        return profit



        