from collections import deque
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        q = deque()
        min_price = [float('inf')] * n  
        q.append([0, 0, src])  
        
        while q:
            price, stop, node = q.popleft()
            
            if stop > k:  
                continue

            for fr, to, pr in flights:
                if node == fr:
                    newprice = pr + price
                    if newprice < min_price[to]:  
                        min_price[to] = newprice
                        q.append([newprice, stop + 1, to])  
        
        return min_price[dst] if min_price[dst] != float('inf') else -1  
