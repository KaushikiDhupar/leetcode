import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        max_heap=[-x for x in piles]
        heapq.heapify(max_heap)
        while k:
            a=-heapq.heappop(max_heap)
            reduced = math.ceil(a / 2)

            heapq.heappush(max_heap,-reduced)
            k=k-1

        res=[-x for x in max_heap]
        return sum(res)
